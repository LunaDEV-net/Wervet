from const import Default

def process_data(data_in: list, const_data: Default) -> dict:
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
                data_dict[beobachtungs_id][i][const_data.POS_STATIONSNAME] = stationsname
                data_dict[beobachtungs_id][i][const_data.POS_OFFIZIELLE_ART] = "Offizielle Art"
                data_dict[beobachtungs_id][i][const_data.POS_TYP] = "TYP"
                data_dict[beobachtungs_id][i][const_data.POS_AUTOMATISCHE_BEZEICHNUNG] = "Automat. Bezeichnung"
                data_dict[beobachtungs_id][i][const_data.POS_BEOBACHTET_BIS_AUTO] = "Beob. bis (MM-JJJJ)"
                data_dict[beobachtungs_id][i][const_data.POS_BERUFSGRUPPE] = "Berufsgruppe (soll nacher überschrieben werden)"
                data_dict[beobachtungs_id][i][const_data.POS_HANDSCHUHE_ERHOBEN] = "Handschuhe erhoben?"
                data_dict[beobachtungs_id][i][const_data.POS_BEOBACHTET_VON] = beobachtet_von
                data_dict[beobachtungs_id][i][const_data.POS_BEOBACHTET_BIS] = beobachtet_bis

                data_dict[beobachtungs_id][i][const_data.POS_BEOBACHTUNGEN_GESAMT] = 0
                data_dict[beobachtungs_id][i][const_data.POS_HDS_GESAMT] = 0

                for key in const_data.indexe_indikatoren:
                    data_dict[beobachtungs_id][i][const_data.indexe_indikatoren[key]] = 0 # Gesamt
                    data_dict[beobachtungs_id][i][const_data.indexe_indikatoren[key]+1] = 0 # HDs
                    data_dict[beobachtungs_id][i][const_data.indexe_indikatoren[key]+2] = 0 # Compliance
                    data_dict[beobachtungs_id][i][const_data.indexe_indikatoren[key]+3] = 0 # HS
            data_dict[beobachtungs_id][0][const_data.POS_BERUFSGRUPPE] = "Gesamt"
            data_dict[beobachtungs_id][1][const_data.POS_BERUFSGRUPPE] = "Ärzte"
            data_dict[beobachtungs_id][2][const_data.POS_BERUFSGRUPPE] = "Pflegepersonal"
            data_dict[beobachtungs_id][3][const_data.POS_BERUFSGRUPPE] = "Andere"


        berufindex = const_data.indexe_berufsgruppen[berufsgruppe]
        if not indikator.startswith("vor asept. Tätigkeit: "):
            indikatorindex = const_data.indexe_indikatoren[indikator]
        elif indikator.startswith("vor asept. Tätigkeit: "):
            indikatorindex = const_data.indexe_indikatoren["vor asept. Tätigkeit: *"]

        # gesamt vorne
        data_dict[beobachtungs_id][0][const_data.POS_BEOBACHTUNGEN_GESAMT] += 1
        data_dict[beobachtungs_id][berufindex][const_data.POS_BEOBACHTUNGEN_GESAMT] += 1
        if hd == "Ja":
            data_dict[beobachtungs_id][0][const_data.POS_HDS_GESAMT] += 1
            data_dict[beobachtungs_id][berufindex][const_data.POS_HDS_GESAMT] += 1
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
            ganzfein_indikatorindex = const_data.indexe_indikatoren[indikator]
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
            for comp_index in const_data.Compliances:
                beob = data_dict[beob_id][i][comp_index-2]
                hds = data_dict[beob_id][i][comp_index-1]
                data_dict[beob_id][i][comp_index] = int(round(hds / beob, 2) * 100) if beob != 0 else 0
                pass
    return data_dict