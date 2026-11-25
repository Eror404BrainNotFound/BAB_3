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