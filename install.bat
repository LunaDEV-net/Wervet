@echo off
echo WebKess Installer (only for Windows)
echo Installing...
echo Installing Windows Package Manager...
git submodule update --init --recursive
echo Python...
winget install Python.Python
echo git...
winget install Git.Git
echo Installing Python virtual environment...
python -m venv .venv