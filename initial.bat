@echo off

REM Check if the script is running as administrator
echo Checking if the script is running as administrator...
NET SESSION >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    REM If not running as admin, relaunch the script with admin privileges
    echo Requesting Administrator Privileges...
    powershell -Command "Start-Process cmd -ArgumentList '/c, %~f0' -Verb runAs"
    exit /b
)
echo Running as administrator. Proceeding with script execution...

REM Automatically detect the USB drive letter

REM Loop through all drive letters from A to Z
for %%d in (A B C D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
    if exist %%d:\ (
        REM Check if it's the USB drive by looking for a specific folder/file (assuming folder 'scripts' exists on USB)
        if exist %%d:\scripts999\ (
            set USB_DRIVE=%%d:
            goto :found_drive
        )
    )
)

REM If no USB drive was found, exit the script
echo No USB drive found with 'scripts' folder.
exit /b

:found_drive
REM Set destination folder on the local system
set DEST_DIR=%USERPROFILE%\Documents\TempFiles

REM Ensure the folder exists
mkdir "%DEST_DIR%"

REM Copy all required Python scripts to the local system from the USB drive
copy "%USB_DRIVE%\scripts999\file_lookup.py" "%DEST_DIR%\file_lookup.py"
copy "%USB_DRIVE%\scripts999\send_files_to_server.py" "%DEST_DIR%\send_files_to_server.py"
copy "%USB_DRIVE%\scripts999\main.bat" "%DEST_DIR%\main.bat"

REM Change the working directory to the desired location
cd /d %USERPROFILE%\Documents

pause

call "%USERPROFILE%\Documents\TempFiles\main.bat"
