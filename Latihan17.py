import platform
import os

os.system('cls')

dict_anak1 = {
    "nama": "Abdel",
    "umur": 15
}

dict_anak2 = {
    "nama": "Temon",
    "umur": 10
}

keluargaBesar = {
    "kami": [dict_anak1, dict_anak2],
    "tante": "andika"
}

print(keluargaBesar)

print(keluargaBesar["kami"][1]["nama"])
print(keluargaBesar["tante"])
print(keluargaBesar["kami"][0]["nama"])

print("Nama Komputer\t:", platform.node())