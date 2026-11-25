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