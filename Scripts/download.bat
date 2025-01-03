@echo off
echo Herunterladen in Dateipfad: %cd%\WebKess
echo.

echo Schaue ob winget vorhanden ist
winget --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Winget ist installiert und funktioniert.
) else (
    echo Winget ist nicht installiert oder funktioniert nicht korrekt. Siehe evt. bei den Systemanforderungen noch mal nach.
)

echo Lade benoetigte Programme runter...
echo - Python...
echo. 
winget install Python.Python.3.13
echo.
echo     - Ueberpruefe Python Instalation
python -V
if %errorlevel% equ 0 (
    echo Python ist richtig installiert
) else (
    echo Fehler: Python nicht richtig installiert.
    exit /b 1
)
echo.
echo.
echo - Git...
echo. 
winget install Git.Git
echo.
echo     - Ueberpruefe GitInstalation
git -v
if %errorlevel% equ 0 (
    echo Git ist richtig installiert
) else (
    echo Fehler: Git nicht richtig installiert.
    exit /b 1
)
echo.
echo.
echo Klonen
echo.
git clone https://github.com/LunaDEV-net/WebKess
echo.
