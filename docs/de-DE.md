# WebKess: Bedienungsanleitung

## Einführung
**WebKess** ist ein lokales Python-Programm, das Rohdaten von [Aktion Saubere Hände](https://www.aktion-sauberehaende.de/ueber-uns-ash) in ein Excel-freundliches Format umwandelt.

---

## Systemanforderungen
- **Windows 11**
- **Windows 10**, mit einer Betriebssystem-Buildnummer > `16299`  
  _Hinweis: Die Buildnummer kann unter `Einstellungen > System > Info` bei den `Windows-Spezifikationen` überprüft werden._

---

## Installation
### mit Downloadscript
**Funktioniert nur auf Windows**
1. Die Release-Website öffnen: https://github.com/LunaDEV-net/WebKess/releases
2. Die Datei `download.bat` herunterladen. <br> <img src="imgs/2025-01-03_WebKess_Manual-Download-bat.jpg">
3. Die heruntergeladene Datei in den Überordner kopieren, wo das Programm hingeladen werden soll: <br> Z.B. Wenn die `download.bat` im Pfad `D:\Programme\download.bat` liegt, dann wird das Programm nach `D:\Programme\WebKess` installiert
4. Sobald die `download.bat` an der gewünschten Stelle liegt, diese im File-Explorer mit einem Doppelklick öffnen.
5. `download.bat` übernimmt die Installation der Software

## Nutzung
1. Laden Sie sich die Rohdaten **(Anleitung TODO)** runter, diese müssen eine `CSV`-Datei sein und das folgende Format haben (Zu Not einmal kurz mit Excel öffnen und überprüfen) 

| KISS-Kürzel | IntervallId | Stationsname | Startdatum | Enddatum | BeobachtungsId | Beobachtungsdatum | Berufsgruppe | Indikation | Aktion | Handschuhe | Import KisRecordId Intervall | Import KisRecordId Beobachtung |
|-------------|-------------|--------------|------------|----------|----------------|-------------------|--------------|------------|--------|------------|------------------------------|--------------------------------|

2. Benennen Sie diese in `input.csv` um und kopieren sie diese in den Ordner `data`. <br> 
- WebKess <br>
  - data\ <br>
    - **input.csv** <br>
  - docs\ <br>
    - de-DE.md <br>
  - example_data\ <br>
  - README.md <br>
  - run.bat <br>
3. Führen Sie die `run.bat` aus, indem Sie diese im File-Explorer mit einem Doppelklick öffnen
4. Sie erhalten ihre Datei im `data` Ordner als `output.csv` <br>
- WebKess <br>
  - data\ <br>
    - input.csv <br>
    - **output.csv** <br>
  - docs\ <br>
    - de-DE.md <br>
  - example_data\ <br>
  - README.md <br>
  - run.bat <br>
---