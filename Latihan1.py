import platform
import os

os.system('cls')

# Sampel-1
list1 = ["apel", 34, True, 40, "pisang"]
print(list1)

# Sampel-2
list2 = ["apel", "pisang", "semangka", "apel", "semangka"]
print(list2)

# Sampel-3
list3 = ["apel", "pisang", "semangka"]
print("Panjang list yaitu", len(list3))
for i in range(len(list3)):
    print(end=list3[i] + " ")
print("")

# Sampel-4
list4 = ["apel", "pisang", "semangka"]
print(type(list4))

# Sampel-5
list5 = list(("apel", "pisang", "semangka"))
print(list5)

print("Nama Komputer\t:", platform.node())