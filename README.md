# USB Autorun for Sensitive Document Exfiltration to Remote Server

## Overview
This project demonstrates a USB-based data exfiltration technique for educational purposes. It highlights potential cybersecurity risks associated with USB drives, specifically focusing on sensitive document discovery, copying, and exfiltration to a remote server.

> **Disclaimer:** This project is strictly for educational use in controlled environments to enhance cybersecurity awareness and improve defenses. Unauthorized or unethical use of this tool is illegal.

---

## Features
- **Automatic Execution:** The `initial.bat` file automates the entire process, requiring no manual setup or external installations.
- **Document Discovery:** Searches for `.docx`, `.pdf`, and `.xlsx` files on the target system. (We can add any extension for file extraction)
- **Secure Remote Transfer:** Exfiltrates files to a remote server via SSH using obfuscated credentials.
- **USB Auto-Detection:** Detects the insertion of a specific USB drive with the `scripts999` folder.
- **Temporary Workspace:** Copies scripts to a temporary folder on the target system for execution.

---

## Purpose
This tool serves as a learning aid for:
- **Cybersecurity Training:** Teaching professionals about USB-based attack vectors.
- **Security Testing:** Evaluating endpoint protection, antivirus, and EDR systems.
- **Research:** Understanding vulnerabilities in physical media.

---

## Requirements
No prerequisites are needed. Simply run the `initial.bat` file located in the USB drive. We ran this file using autorun. You need to figure it out yourself.

Also Update the credentials of your server in `send_files_to_server.py` file. You can use any cloud machine or your own self hosted machine.

### Why the `scripts999` Folder is Important
The `scripts999` folder acts as the unique identifier for the USB drive. The `initial.bat` file uses this folder to:
- Detect the correct USB drive during insertion.
- Copy required scripts (`file_lookup.py`, `send_files_to_server.py`, and `main.bat`) to the local system.
- Ensure proper functioning of the project by maintaining consistency in file locations.

**Note:** If the folder is missing or renamed, the script will fail to detect the USB drive. Also you can rename it to any string, just change it in initial.bat

---

## Installation
1. **Prepare the USB Drive:**
   - Copy the `initial.bat` file and the `scripts999` folder (containing the necessary Python scripts) to the root directory of the USB drive.
   - Ensure the USB drive is formatted as FAT32 for compatibility.

2. **Run the `initial.bat` File:**
   - Insert the USB drive into the target system.
   - If autorun is present it will execute the initial.bat file or else you have to click it yourself.

---

## Key Steps in `initial.bat` File
1. **Administrator Privilege Check:** Ensures the script runs with elevated privileges.
2. **USB Drive Detection:** Locates the USB drive using the presence of the `scripts999` folder.
3. **Script Copying:** Copies all necessary scripts from the USB drive to a temporary folder (`TempFiles`) on the target system. (This step is done so that in case someone plugs out the usb our system still works)
4. **Execution:** Executes the main script (`main.bat`) to initiate the file discovery and exfiltration process.

---

## Collaborators
- **Saad Bukhari** ([GitHub](https://github.com/saadbukhari00))
- **Abdul Rafay**  ([GitHub](https://github.com/abdulrafay1-4))

---

## Example Scenario
1. Deploy the tool on a virtual machine with sample sensitive documents.
2. Insert the USB drive and run the `initial.bat` file.
3. Observe the automated workflow:
   - Discovery of sensitive files.
   - Secure transfer of files to the remote server.
   - Cleanup of temporary files after execution.

---

## Key Features
- **File Discovery and Exfiltration:** Identifies and transfers sensitive files from the target system.
- **Automated Execution:** Eliminates manual setup requirements.
- **Obfuscation:** Uses Base64 encoding for sensitive data to bypass basic security checks.
- **Robust Cleanup:** Ensures no traces remain after execution.

---

## Future Work
- Make Python script that work with linux and mac.
- Replace bat scripts with sh to make it working in linux.
- Implement file obfuscation for data exfiltration.

## Ethical Use
This project is intended solely for educational purposes. Unethical use, such as unauthorized access or data exfiltration, is strictly prohibited and punishable by law.

---

## References
- [Python Documentation](https://www.python.org/doc/)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [Paramiko Library](http://docs.paramiko.org/en/stable/)

For additional queries, feel free to contact the collaborators.

