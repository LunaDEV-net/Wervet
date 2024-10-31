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

    Compliances: list = [
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

    number_of_colums = 14
    should_not_be_empty_colums = [0,1,2,3,4,5,6,7,8,9] # [x for x in range(0, 10+1)]
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
    handschue = 10

class Custom:
    pass
