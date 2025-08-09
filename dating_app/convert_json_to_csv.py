import json
import csv

# File input/output
json_file = "data/users.json"
csv_file = "data/users.csv"

# Baca file JSON
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Ambil header dari key JSON pertama
header = data[0].keys()

# Tulis ke file CSV
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)

print(f"Data berhasil dikonversi ke {csv_file}")
