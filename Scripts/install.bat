@echo off
rem check if path is correct (only the explorer)
rem https://stackoverflow.com/a/32423352
for %%a in ("%~dp0\.") do set "parent=%%~nxa"
if %parent%==Scripts echo switch to partent dir
if %parent%==Scripts cd ..
rem should the in WebKess Folder


echo WebKess Installer (only for Windows)
echo Installing...
echo Python...
winget install Python.Python
echo git...
winget install Git.Git
echo Installing Python virtual environment...
python -m venv .venv