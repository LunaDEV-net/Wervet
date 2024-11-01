class Default:
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

    compliance: list = [
        11,  # Compliance Gesamt
        indexe_indikatoren['vor Kontakt mit Patienten'] + 2,  # Compliance vor Pat.-Kontakt
        indexe_indikatoren['vor asept. Tätigkeit: *'] + 2,  # Compliance vor asept. Tät.
        indexe_indikatoren['nach Kontakt mit pot. infekt. Material'] + 2,  # Compliance nach Material
        indexe_indikatoren['nach Kontakt mit Patienten'] + 2,  # Compliance nach Pat.-Kontakt
        indexe_indikatoren['nach Kontakt mit Pat.-Umgebung'] + 2,  # Compliance nach Umgebung

        indexe_indikatoren['vor asept. Tätigkeit: Beatmung'] + 2,  # Compliance Beatmung
        indexe_indikatoren['vor asept. Tätigkeit: i.v. Med. zubereiten'] + 2,  # Compliance Med.zub.
        indexe_indikatoren['vor asept. Tätigkeit: Manip. i.v./i.a. Zugänge'] + 2,  # Compliance Zugänge
        indexe_indikatoren['vor asept. Tätigkeit: Verbandw., Manip. Drain.'] + 2,  # Compliance Verb/Drg.
        indexe_indikatoren['vor asept. Tätigkeit: Punktionen, Zugänge legen'] + 2,  # Compliance Punktionen
        indexe_indikatoren['vor asept. Tätigkeit: Schleimhautkontakt'] + 2,  # Compliance Schleimhaut
        indexe_indikatoren['vor asept. Tätigkeit: keine Angabe'] + 2,  # Compliance sonstige
    ]

    # number_of_columns = 14
    should_not_be_empty_columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # [x for x in range(0, 10+1)]
    disallowed_characters = ["*"]

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

    # indexe
    beobachtungs_id = 1
    stationsname = 2
    beobachtet_von = 3
    beobachtet_bis = 4
    berufsgruppe = 7
    indikator = 8
    hd = 9
    handschuhe = 10

    header = [
        "Header: Stationsname", "Offizielle Art", "TYP", "Automat. Bezeichnung", "Beob. bis (MM-JJJJ)", "Berufsgruppe", "Handschuhe erhoben", "Beobachtet von", "Beobachtet bis", "Beobachtungen gesamt", "HDS gesamt", "Compliance gesamt",
        "Ref 10.%tile", "Ref. 25.%tile","Ref. Median","Ref. 75.%tile","Ref. 90%tile","Ref. Handschuhe","Nicht indizierte HD",
        "Beob vor Pat.-Kontakt", "HDs vor Pat.-Kontakt", "Compl. vor Pat.-Kontakt", "Absolut: HS vor Pat.-Kontakt",
        "Beob vor asept. Tät.", "HDs vor asept. Tät.", "Compl. vor asept. Tät.", "Absolut:HS vor asept. Tät.",
        "Beob nach Material", "HDs nach Material", "Compl. nach Material", "Absolut:HS nach Material",
        "Beob nach Pat.-Kontakt", "HDs nach Pat.-Kontakt", "Compl. nach Pat.-Kontakt", "Absolut:HS nach Pat.-Kontakt",
        "Beob nach Pat.-Umgebung", "HDs nach Pat.-Umgebung", "Compl. nach Pat.-Umgebung", "Absolut:HS nach Pat.-Umgebung",
        "Beob vor Beatmung", "HDs vor Beatmung", "Compl. vor Beatmung", "Absolut:HS vor Beatmung",
        "Beob vor Med.zub.", "HDs vor Med.zub.", "Compl. vor Med.zub.", "Absolut:HS vor Med.zub.",
        "Beob vor Zugänge", "HDs vor Zugänge", "Compl. vor Zugänge", "Absolut:HS vor Zugänge",
        "Beob vor Verb/Drg.", "HDs vor Verb/Drg.", "Compl. vor Verb/Drg.", "Absolut:HS vor Verb/Drg.",
        "Beob vor Punktionen", "HDs vor Punktionen", "Compl. vor Punktionen", "Absolut:HS vor Punktionen",
        "Beob vor Schleimhaut", "HDs vor Schleimhaut", "Compl. vor Schleimhaut", "Absolut:HS vor Schleimhaut",
        "Beob vor sonstige", "HDs vor sonstige", "Compl. vor sonstige", "Absolut:HS vor sonstige",
    ]

class Custom:
    pass
