indexe_indikatoren: dict = {
    'vor Kontakt mit Patienten': 19,
    'vor asept. Tätigkeit: *': 23,
    'nach Kontakt mit pot. infekt. Material': 27,
    'nach Kontakt mit Patienten': 31,
    'nach Kontakt mit Pat.-Umgebung': 35,

    'vor asept. Tätigkeit: Beatmung': 39,
    'vor asept. Tätigkeit: i.v. Med. zubereiten': 43,
    'vor asept. Tätigkeit: Manip. i.v./i.a. Zugänge': 47,
    'vor asept. Tätigkeit: Verbandw., Manip. Drain.': 51,
    'vor asept. Tätigkeit: Punktionen, Zugänge legen': 55,
    'vor asept. Tätigkeit: Schleimhautkontakt': 59,
    'vor asept. Tätigkeit: keine Angabe': 63,
}
indexe_berufsgruppen: dict = {
    'Ärzte': 1,
    'Pflegepersonal': 2,
    'Andere': 3,
}

Compliances: list = [
    11, #Compliance Gesamt
    indexe_indikatoren['vor Kontakt mit Patienten'] + 2, # Compliance vor Pat.-Kontakt
    indexe_indikatoren['vor asept. Tätigkeit: *'] + 2, # Compliance vor asept. Tät.
    indexe_indikatoren['nach Kontakt mit pot. infekt. Material'] + 2, # Compliance nach Material
    indexe_indikatoren['nach Kontakt mit Patienten'] + 2, # Compliance nach Pat.-Kontakt
    indexe_indikatoren['nach Kontakt mit Pat.-Umgebung'] + 2, # Compliance nach Umgebung

    indexe_indikatoren['vor asept. Tätigkeit: Beatmung'] + 2, # Compliance Beatmung
    indexe_indikatoren['vor asept. Tätigkeit: i.v. Med. zubereiten'] + 2, # Compliance Med.zub.
    indexe_indikatoren['vor asept. Tätigkeit: Manip. i.v./i.a. Zugänge'] + 2, # Compliance Zugänge
    indexe_indikatoren['vor asept. Tätigkeit: Verbandw., Manip. Drain.'] + 2, # Compliance Verb/Drg.
    indexe_indikatoren['vor asept. Tätigkeit: Punktionen, Zugänge legen'] + 2, # Compliance Punktionen
    indexe_indikatoren['vor asept. Tätigkeit: Schleimhautkontakt'] + 2, # Compliance Schleimhaut
    indexe_indikatoren['vor asept. Tätigkeit: keine Angabe'] + 2, # Compliance sonstige
]

# const
POS_STATIONSNAME = 0
POS_OFFIZIELLE_ART = 1
POS_TYP = 2
POS_AUTOMATISCHE_BEZEICHNUNG = 3
POS_BEOBACHTET_BIS_AUTO = 4
POS_BERUFSGRUPPE = 5
POS_HANDSCHUHE_ERHOBEN = 6
POS_BEOBACHTET_VON = 7
POS_BEOBACHTET_BIS = 8

POS_BEOBACHTUNGEN_GESAMT = 9
POS_HDS_GESAMT = 10

def process_data(data_in: list) -> dict:
    data_dict: dict = {}
    for line in data_in:
        beobachtungs_id = line[1]
        stationsname = line[2]
        beobachtet_von = line[3]
        beobachtet_bis = line[4]
        berufsgruppe = line[7]
        indikator = line[8]
        hd = line[9]
        handschue = line[10]
        #setup
        if data_dict.get(beobachtungs_id) == None: # Wenn es noch kein Eintrag für die BeobachtungsID gibt
            data_dict[beobachtungs_id] = [[],[],[],[]] # erstelle die zeilen gesamt, ärzte, pflege, andere
            for i in range(67):
                data_dict[beobachtungs_id][0].append(None) # fülle die zeilen
                data_dict[beobachtungs_id][1].append(None) # fülle die zeilen
                data_dict[beobachtungs_id][2].append(None) # fülle die zeilen
                data_dict[beobachtungs_id][3].append(None) # fülle die zeilen
            # gebe erste daten ein
            for i in range(4):
                data_dict[beobachtungs_id][i][POS_STATIONSNAME] = stationsname
                data_dict[beobachtungs_id][i][POS_OFFIZIELLE_ART] = "Offizielle Art"
                data_dict[beobachtungs_id][i][POS_TYP] = "TYP"
                data_dict[beobachtungs_id][i][POS_AUTOMATISCHE_BEZEICHNUNG] = "Automat. Bezeichnung"
                data_dict[beobachtungs_id][i][POS_BEOBACHTET_BIS_AUTO] = "Beob. bis (MM-JJJJ)"
                data_dict[beobachtungs_id][i][POS_BERUFSGRUPPE] = "Berufsgruppe (soll nacher überschrieben werden)"
                data_dict[beobachtungs_id][i][POS_HANDSCHUHE_ERHOBEN] = "Handschuhe erhoben?"
                data_dict[beobachtungs_id][i][POS_BEOBACHTET_VON] = beobachtet_von
                data_dict[beobachtungs_id][i][POS_BEOBACHTET_BIS] = beobachtet_bis

                data_dict[beobachtungs_id][i][POS_BEOBACHTUNGEN_GESAMT] = 0
                data_dict[beobachtungs_id][i][POS_HDS_GESAMT] = 0

                for key in indexe_indikatoren:
                    data_dict[beobachtungs_id][i][indexe_indikatoren[key]] = 0 # Gesamt
                    data_dict[beobachtungs_id][i][indexe_indikatoren[key]+1] = 0 # HDs
                    data_dict[beobachtungs_id][i][indexe_indikatoren[key]+2] = 0 # Compliance
                    data_dict[beobachtungs_id][i][indexe_indikatoren[key]+3] = 0 # HS
            data_dict[beobachtungs_id][0][POS_BERUFSGRUPPE] = "Gesamt"
            data_dict[beobachtungs_id][1][POS_BERUFSGRUPPE] = "Ärzte"
            data_dict[beobachtungs_id][2][POS_BERUFSGRUPPE] = "Pflegepersonal"
            data_dict[beobachtungs_id][3][POS_BERUFSGRUPPE] = "Andere"


        berufindex = indexe_berufsgruppen[berufsgruppe]
        if not indikator.startswith("vor asept. Tätigkeit: "):
            indikatorindex = indexe_indikatoren[indikator]
        elif indikator.startswith("vor asept. Tätigkeit: "):
            indikatorindex = indexe_indikatoren["vor asept. Tätigkeit: *"]

        # gesamt vorne
        data_dict[beobachtungs_id][0][POS_BEOBACHTUNGEN_GESAMT] += 1
        data_dict[beobachtungs_id][berufindex][POS_BEOBACHTUNGEN_GESAMT] += 1
        if hd == "Ja":
            data_dict[beobachtungs_id][0][POS_HDS_GESAMT] += 1
            data_dict[beobachtungs_id][berufindex][POS_HDS_GESAMT] += 1
        # GIbt kein Feld für Handschue vorne

        # fein
        data_dict[beobachtungs_id][0][indikatorindex] += 1 # Gesamt Job egal
        data_dict[beobachtungs_id][berufindex][indikatorindex] += 1 # Gesamt Job spez
        if hd == "Ja":
            data_dict[beobachtungs_id][0][indikatorindex+1] += 1 # HDs Job egal
            data_dict[beobachtungs_id][berufindex][indikatorindex+1] += 1 # HDs. Job spez
        if handschue == "Ja":
            data_dict[beobachtungs_id][0][indikatorindex+3] += 1 # HDs Job egal
            data_dict[beobachtungs_id][berufindex][indikatorindex+3] += 1 # HDs. Job spez

        if indikator.startswith("vor asept. Tätigkeit: "):
            ganzfein_indikatorindex = indexe_indikatoren[indikator]
            data_dict[beobachtungs_id][0][ganzfein_indikatorindex] += 1  # Gesamt Job egal
            data_dict[beobachtungs_id][berufindex][ganzfein_indikatorindex] += 1  # Gesamt Job spez
            if hd == "Ja":
                data_dict[beobachtungs_id][0][ganzfein_indikatorindex + 1] += 1  # HDs Job egal
                data_dict[beobachtungs_id][berufindex][ganzfein_indikatorindex + 1] += 1  # HDs. Job spez
            if handschue == "Ja":
                data_dict[beobachtungs_id][0][ganzfein_indikatorindex + 3] += 1  # HDs Job egal
                data_dict[beobachtungs_id][berufindex][ganzfein_indikatorindex + 3] += 1  # HDs. Job spez

    for beob_id in data_dict.keys():
        for i in range(len(data_dict[beob_id])): # len(beob_id) = 4
            for comp_index in Compliances:
                beob = data_dict[beob_id][i][comp_index-2]
                hds = data_dict[beob_id][i][comp_index-1]
                data_dict[beob_id][i][comp_index] = int(round(hds / beob, 2) * 100) if beob != 0 else 0
                pass
    return data_dict