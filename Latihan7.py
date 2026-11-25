import platform
import os

os.system('cls')

# Sampel-1
list1 = ["apel", "pisang", "semangka"]
list2 = ["jeruk", "kiwi", "melon", "mangga"]

list1.extend(list2)
print(list1)

# Sampel-2
list3 = ["apel", "pisang", "semangka", "jeruk", "kiwi", "melon", "mangga"]

try:
    cari = list3.index("kiwi")
    print("Ada di index ke", cari)
except ValueError:
    print("Tidak ditemukan")

# Sampel-3
list4 = ["apel", "pisang", "semangka", "jeruk", "kiwi", "melon", "mangga"]
list4.reverse()
print(list4)

# Sampel-4
list5 = ["apel", "pisang", "semangka", "jeruk", "kiwi", "melon", "mangga"]
list5.sort(reverse=True)
print(list5)

print("Nama Komputer\t:", platform.node())