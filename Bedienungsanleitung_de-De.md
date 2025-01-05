# Wervet: Bedienungsanleitung

## Übersicht
**Wervet** ist ein lokales Python-Programm, das Rohdaten von [Aktion Saubere Hände](https://www.aktion-sauberehaende.de/ueber-uns-ash) in ein Excel Format umwandelt. Dieses Dokument bietet eine Anleitung zur Installation und Nutzung des Programms.
---

## Systemanforderungen
- **Windows 11**
- **Windows 10**, mit einer Betriebssystem-Buildnummer über `16299`  
  _Hinweis: Die Buildnummer kann unter `Einstellungen > System > Info` bei den `Windows-Spezifikationen` überprüft werden._
---
## Installation
### Installation über Download-Script
**Hinweis:** Dieses Verfahren funktioniert nur auf Windows.

1. Besuchen Sie die [Release-Website](https://github.com/LunaDEV-net/Wervet/releases).

2. Laden Sie die Datei `download.bat` in den Pfad herunter, in welchen der Arbeitsordner erstellt werden soll, z.B. `dieser PC > lokaler Datenträger > persönliche Daten` <br> ![Download-Screenshot](https://raw.githubusercontent.com/LunaDEV-net/Wervet/main/docs/imgs/2025-01-03_WebKess_Manual-Download-bat.jpg)

3. Führen Sie durch Doppelclick dieses Programm aus. Es wird ein Ordner `Wervet` mit den notwendigen Programmdaten erstellt.

   4. Es öffnet sich ein Fenster. Auf `weitere Informationen` klicken. Dann auf `trotzdem ausführen` klicken.

5. Danach kann die `download.bat` gelöscht werden.

---

## Nutzung
Beispiel Struktur des Programms
   ```
   Wervet
   ├─ data\
   │   ├─ input.csv
   │   └─ output.csv
   ├─ docs\
   │   └─ de-DE.md
   ├─ README.md
   └─ run.bat
   ```

1. Rohdaten vorbereiten: Laden Sie die Rohdaten herunter. Die Datei muss im CSV-Format vorliegen und sollte folgendes Schema aufweisen (zur Sicherheit mit Excel öffnen und überprüfen):

   | KISS-Kürzel | IntervallId | Stationsname | Startdatum | Enddatum | BeobachtungsId | Beobachtungsdatum | Berufsgruppe | Indikation | Aktion | Handschuhe | Import KisRecordId Intervall | Import KisRecordId Beobachtung |
   |-------------|-------------|--------------|------------|----------|----------------|-------------------|--------------|------------|--------|------------|------------------------------|--------------------------------|


2. Öffnen Sie den Datei-Explorer und navigieren Sie Ordner, in dem Sie das Wervet-Tool abgelegt haben.

3. Kopieren Sie die heruntergeladene WebKess-Rohdaten-Datei in den Ordner `data` und benennen Sie sie in `input.csv` (Auf Groß- & Kleinschreibung achten!) um. Sollte bereits eine `input.csv` im Ordner vorhanden sein, achten Sie darauf, dass Sie die alte `input.csv` zuvor umbenennen oder löschen.

4. Programm ausführen Führen Sie die Datei `run.bat` im Wervet-Ordner aus, indem Sie diese im Datei-Explorer per Doppelklick öffnen. Nach Durchlaufen des Programmes, durch Drücken der Entertaste in der Kommandozeile das Programm beenden.

5. Nach der Verarbeitung wird die bearbeitete Datei als `output.csv` im Ordner `data` gespeichert. **Diese wird bei jedem Programmstart überschrieben und sollte daher sofort in einen anderen Ordner gesichert werden!**

6. Ergebnisse in Excel öffnen