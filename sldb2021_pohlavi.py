import csv

IN_FILE = "data/sldb2021_pohlavi.csv"
OUT_FILE = "out/sldb2021_pohlavi.csv"

OUT_HEADER = [
    "id_objekt",
    "id_filtr",
    "id_promenna",
    "id_komb_kategorie",
    "platnost_od",
    "platnost_do",
    "hodnota",
    "id_jednotka",
    "pozn",
]

ID_TYP_OBJEKTU = {
    "43": "obec",
    "44": "mestka_cast",
    "65": "orp",
    "72": "spravni_obvod_v_praze",  # ??
    "97": "stat",  
    "99": "oblast",  # ??
    "100": "kraj",
    "101": "okres",
}

ID_FILTR = {
    "1": "sex_M",
    "2": "sex_F",
}

DEFAULT = {
    "id_promenna": "02_pocetObyvatel",
    "id_komb_kategorie": None,
    "platnost_od": "2021-01-01",
    "platnost_do": "2021-12-31",
    "id_jednotka": "count",
    "pozn": "Obyvatelstvo podle pohlaví zdroj: https://www.czso.cz/documents/62353418/182807150/sldb2021_pohlavi.csv"
}


with open(IN_FILE) as in_f, open(OUT_FILE, "w") as out_f:
    reader = csv.DictReader(in_f)
    writer = csv.DictWriter(out_f, OUT_HEADER)
    writer.writeheader()
    for line in reader:
        if ID_TYP_OBJEKTU.get(line["uzemi_cis"]) not in ("obec", "mestska_cast"):
            continue
        d = DEFAULT.copy()
        d["id_objekt"] = line["uzemi_kod"]
        d["id_filtr"] = ID_FILTR.get(line["pohlavi_kod"])
        d["hodnota"] = line["hodnota"]
        writer.writerow(d)