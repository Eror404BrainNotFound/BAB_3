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

print("Nama Komputer\t:", platform.node())