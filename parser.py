import csv
import json

adatok = []

with open("anyagok.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    for sor in reader:
        anyag, ar, csere = sor
        adatok.append({
            "anyag": anyag,
            "ar": int(ar),
            "csere": int(csere)
        })

with open("adatok.json", "w", encoding="utf-8") as jsonfile:
    json.dump(adatok, jsonfile, indent=4, ensure_ascii=False)

print("Adatok Feldolgozva")