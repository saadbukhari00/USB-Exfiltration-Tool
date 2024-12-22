@echo on


REM Check if Python is installed
echo Checking if Python is installed...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    REM Python is not installed, so we proceed to download and install it
    echo Python is not installed. Downloading and installing Python...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.10.4/python-3.10.4.exe' -OutFile 'python_installer.exe'"

    REM Run the Python installer silently and install Python
    echo Installing Python...
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 >nul 2>&1

    REM Clean up by deleting the installer
    echo Deleting Python installer...
    del python_installer.exe >nul 2>&1

    REM Check if the installation was successful
    python --version >nul 2>&1
    IF %ERRORLEVEL% NEQ 0 (
        echo Python installation failed. Exiting...
        exit /b
    )
    echo Python installed successfully.
)

REM Upgrade pip and ensure dependencies are installed
echo Upgrading pip...
python -m ensurepip --upgrade >nul 2>&1
python -m pip install --upgrade pip >nul 2>&1

echo Installing required dependencies...
python -m pip install paramiko >nul 2>&1

REM Define the local folder where files will be copied temporarily
set TEMP_FOLDER=%USERPROFILE%\Documents\TempFiles
echo Defining temporary folder at %TEMP_FOLDER%

REM Execute the Python script
echo Running the main Python script...
python "%TEMP_FOLDER%\file_lookup.py"

pause

python "%TEMP_FOLDER%\send_files_to_server.py"

pause

REM Clean up by deleting the copied scripts and files
echo Cleaning up temporary files...
del /f /q "%TEMP_FOLDER%\file_lookup.py"
del /f /q "%TEMP_FOLDER%\send_files_to_server.py"
del /f /q "%TEMP_FOLDER%\main.bat"

REM Optionally delete the temporary folder (if you don't want it to persist)
echo Deleting temporary folder...
rmdir /s /q "%TEMP_FOLDER%"

echo Script execution completed successfully.
pause
