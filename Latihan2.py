import platform
import os

os.system('cls')

# Sampel-1
list1 = ["apel", "pisang", "semangka"]
print(list1[1])

# Sampel-2
list2 = ["apel", "pisang", "semangka"]
print(list2[-1])

# Sampel-3
list3 = ["apel", "pisang", "semangka"]

if "apel" in list3:
    print("iya, data 'apel' ada didalam array list")

for x in list3:
    if "g" in x:
        print("iya, huruf 'g' pada list dengan data", x)

print("Nama Komputer\t:", platform.node())