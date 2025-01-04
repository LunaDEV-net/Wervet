@echo off
rem check if path is correct (only the explorer)
rem https://stackoverflow.com/a/32423352
for %%a in ("%~dp0\.") do set "parent=%%~nxa"
if %parent%==Scripts echo switch to partent dir
if %parent%==Scripts cd ..
rem should the in Wervet Folder

git pull
echo success
PAUSE