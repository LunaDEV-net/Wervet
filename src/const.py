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
    indexe_indikatoren: dict = {}
    indexe_berufsgruppen: dict = {}
    Compliances: list = []
    # const
    POS_STATIONSNAME = None
    POS_OFFIZIELLE_ART = None
    POS_TYP = None
    POS_AUTOMATISCHE_BEZEICHNUNG = None
    POS_BEOBACHTET_BIS_AUTO = None
    POS_BERUFSGRUPPE = None
    POS_HANDSCHUHE_ERHOBEN = None
    POS_BEOBACHTET_VON = None
    POS_BEOBACHTET_BIS = None

    POS_BEOBACHTUNGEN_GESAMT = None
    POS_HDS_GESAMT = None

    # indexe
    beobachtungs_id = None
    stationsname = None
    beobachtet_von = None
    beobachtet_bis = None
    berufsgruppe = None
    indikator = None
    hd = None
    handschue = None

    def __init__(self, indexe_indikatoren: dict, indexe_berufsgruppen: dict, Compliances: list, POS_STATIONSNAME: int, POS_OFFIZIELLE_ART: int, POS_TYP: int, POS_AUTOMATISCHE_BEZEICHNUNG: int, POS_BEOBACHTET_BIS_AUTO: int, POS_BERUFSGRUPPE: int, POS_HANDSCHUHE_ERHOBEN: int, POS_BEOBACHTET_VON: int, POS_BEOBACHTET_BIS: int, POS_BEOBACHTUNGEN_GESAMT: int, POS_HDS_GESAMT: int):
        self.indexe_indikatoren = indexe_indikatoren
        self.indexe_berufsgruppen = indexe_berufsgruppen
        self.Compliances = Compliances
        self.POS_STATIONSNAME = POS_STATIONSNAME
        self.POS_OFFIZIELLE_ART = POS_OFFIZIELLE_ART
        self.POS_TYP = POS_TYP
        self.POS_AUTOMATISCHE_BEZEICHNUNG = POS_AUTOMATISCHE_BEZEICHNUNG
        self.POS_BEOBACHTET_BIS_AUTO = POS_BEOBACHTET_BIS_AUTO
        self.POS_BERUFSGRUPPE = POS_BERUFSGRUPPE
        self.POS_HANDSCHUHE_ERHOBEN = POS_HANDSCHUHE_ERHOBEN
        self.POS_BEOBACHTET_VON = POS_BEOBACHTET_VON
        self.POS_BEOBACHTET_BIS = POS_BEOBACHTET_BIS
        self.POS_BEOBACHTUNGEN_GESAMT = POS_BEOBACHTUNGEN_GESAMT
        self.POS_HDS_GESAMT = POS_HDS_GESAMT
