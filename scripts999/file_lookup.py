import os
import shutil
import string

# Allowed file extensions
ALLOWED_EXTENSIONS = {'.pdf', '.xlsx', '.docx'}

def get_all_drives():
    """Detect all available drives in the system."""
    drives = []
    for letter in string.ascii_uppercase:
        drive = f"{letter}:\\"  # Check each drive letter
        if os.path.exists(drive):  # Only add if the drive exists
            drives.append(drive)
    return drives

def is_valid_file(file_path):
    """Check if the file has an allowed extension."""
    return any(file_path.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS)

def copy_files(src, dst, limit=2):
    """Recursively copy filtered files from src to dst, limiting to 'limit' files."""
    files_copied = 0  # To track how many files have been copied
    for foldername, subfolders, filenames in os.walk(src):
        # Avoid scanning the destination folder itself (temp_files)
        if foldername == dst:
            continue
        
        for filename in filenames:
            if files_copied >= limit:  # Stop copying after the limit
                return
            
            src_file = os.path.join(foldername, filename)
            if is_valid_file(src_file):  # Only copy if valid file type
                dst_file = os.path.join(dst, os.path.relpath(src_file, src))
                os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                try:
                    shutil.copy2(src_file, dst_file)
                    files_copied += 1
                    print(f"Copied: {src_file}")
                except Exception as e:
                    print(f"Error copying {src_file}: {e}")

def collect_files(temp_folder="temp_files", limit=2):
    """Collect files from all drives and save them in a temp folder."""
    # Ensure the temp folder is created in the user's Documents directory
    documents_folder = os.path.join(os.environ["USERPROFILE"], "Documents")
    temp_folder_path = os.path.join(documents_folder, temp_folder)
    
    os.makedirs(temp_folder_path, exist_ok=True)
    print(f"Temporary folder created at {temp_folder_path}")
    
    drives = get_all_drives()
    print(f"Detected drives: {drives}")
    
    for drive in drives:
        print(f"Scanning drive {drive}...")
        copy_files(drive, temp_folder_path, limit)
    
    print(f"Files collected in {temp_folder_path}")

if __name__ == "__main__":
    collect_files()
