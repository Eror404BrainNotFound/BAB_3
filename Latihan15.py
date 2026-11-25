import platform
import os

os.system('cls')

# Sampel-1
dict1 = {
    "merk": "Honda",
    "tahun": 2013,
    "tahun": 2020
}

print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# Sampel-2
dict2 = {
    "merk": "Honda",
    "manual": True,
    "tahun": 2013,
    "warna": ["merah", "putih"]
}

print(dict2["warna"][1])
print(dict2["merk"])

# Sampel-3
dict3 = {
    "merk": "Honda",
    "tahun": 1964
}

for i in dict3.keys():
    print(i, end=" ")
print()

for j in dict3.values():
    print(j, end=" ")
print()

for k, v in dict3.items():
    print(k, v)

print("Nama Komputer\t:", platform.node())