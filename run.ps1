echo "Jans WebKess auf Windows Powershell"
echo "in venv gehen"
.\.venv\Scripts\Activate.ps1
echo "main ausführen in standart configuration (data Ordner)"
python .\src\main.py .\data\input.csv .\data\output.csv
echo "fertig, zum Beenden Enter drücken"
PAUSE