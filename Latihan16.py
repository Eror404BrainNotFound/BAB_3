import platform
import os

os.system('cls')

# Sampel-1
dict1 = {
    "merk": "Honda",
    "manual": True,
    "tahun": 2013,
    "warna": ["merah", "putih"]
}

dict1["warna"][1] = "hitam"
dict1.update({"tahun": 2020})

print(dict1)

# Sampel-2
dict2 = {
    "merk": "Honda",
    "manual": True,
    "tahun": 2013,
    "warna": ["merah", "putih"]
}

dict2["warna"].append("hitam")
dict2["tahun"] = 2020
dict2["nama"] = "Brio"

print(dict2)

# Sampel-3
dict3 = {
    "merk": "Honda",
    "manual": True,
    "tahun": 2013,
    "warna": ["merah", "putih"]
}

dict3.popitem()
print(dict3)

# Sampel-4
dict4 = dict2.copy()
dict4.pop("manual")
print(dict4)

# Sampel-5
dict5 = dict2.copy()
dict5.clear()
print(dict5)

print("Nama Komputer\t:", platform.node())