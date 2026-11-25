import platform
import os

os.system('cls')

# Sampel-1
tuple1 = ("apel", "pisang", "semangka")
print(tuple1[1])

# Sampel-2
tuple2 = ("apel", "pisang", "semangka")
print(tuple2[-1])

# Sampel-3
tuple3 = ("apel", "pisang", "semangka")

if "apel" in tuple3:
    print("iya, data 'apel' ada didalam array tuple")

for x in tuple3:
    if "g" in x:
        print("iya, huruf 'g' pada tuple dengan data", x)

print("Nama Komputer\t:", platform.node())




# Latihan 10 - Latihan10.py

import platform
import os

os.system('cls')

# Sampel-1
tuple1 = ("apel", "pisang", "semangka", "jeruk", "kiwi", "melon", "mangga")
tuple2 = ("buah naga", "pepaya")

tuple3 = tuple1 + tuple2
print(tuple3)

# Sampel-2
tuple4 = ("apel", "pisang", "semangka", "jeruk", "kiwi", "melon", "mangga")

try:
    cari = tuple4.index("kiwi")
    print("Ada di index ke", cari)
except ValueError:
    print("Tidak ditemukan")

# Sampel-3
tuple5 = (3, 5, 4, 9, 9, 2, 3, 2, 9)
print(tuple5.count(5))

print("Nama Komputer\t:", platform.node())




# Latihan 11 - Latihan11.py

import platform
import os

os.system('cls')

# Sampel-1
set1 = {"apel", 34, True, 40.45, "pisang"}
print(set1)

# Sampel-2
set2 = {"apel", "pisang", "semangka", "apel", "semangka"}
print(set2)

# Sampel-3
set3 = {"apel", "pisang", "semangka"}

for i in set3:
    print(end=i + " ")
print()

# Sampel-4
set4 = {"apel", "pisang", "semangka"}
print(type(set4))

# Sampel-5
set5 = set(("apel", "pisang", "semangka"))
print(set5)

# Sampel-6
set6 = {"apel", "pisang", "semangka"}

print("Nama Komputer\t:", platform.node())




# Latihan 12 - Latihan12.py

import platform
import os

os.system('cls')

# Sampel-1
set1 = {"apel", "pisang", "semangka"}
set1.add("jeruk")
print(set1)

# Sampel-2
set2 = {"apel", "pisang", "semangka"}
set3 = {"nanas", "mangga", "pepaya"}

set2.update(set3)
print(set2)

# Sampel-3
set4 = {"a", "b", "c"}
tuple1 = ("Ani", "Budi")
list1 = ["apel", "pisang", "semangka"]

my_union_set = set4.union(tuple1, list1)
print(my_union_set)

# Sampel-4
set5 = {"apel", "pisang", "semangka"}

cek = "semangka" in set5
print("Apakah benar data semangka tersebut ada ?", cek)

print("Nama Komputer\t:", platform.node())



# Latihan 13 - Latihan13.py

import platform
import os

os.system('cls')

# Sampel-1
set1 = {"apel", "pisang", "kiwi"}
set1.remove("pisang")
print(set1)

# Sampel-2
set2 = {"apel", "pisang", "kiwi"}
set2.discard("pisang")
print(set2)

# Sampel-3
set3 = {"apel", "pisang", "kiwi"}
set3.pop()
print(set3)

# Sampel-4
set4 = {"apel", "pisang", "kiwi"}
set4.clear()
print(set4)

print("Nama Komputer\t:", platform.node())




# Latihan 14 - Latihan14.py

import platform
import os

os.system('cls')

# Sampel-1
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

set3 = set1.difference(set2)
print("Hasil Difference yaitu", set3)

# Sampel-2
set4 = {1, 2, 3, 4}
set5 = {3, 4, 5}

set6 = set4.symmetric_difference(set5)
print("Hasil Symmetric Difference yaitu", set6)

# Sampel-3
set7 = {"apel", "pisang", "semangka"}
set8 = {"google", "microsoft", "apel"}

set9 = set7.intersection(set8)
print("Hasil Intersection yaitu", set9)

print("Nama Komputer\t:", platform.node())




# Latihan 15 - Latihan15.py

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



# Latihan 16 - Latihan16.py

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




# Latihan 17 - Latihan17.py

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
