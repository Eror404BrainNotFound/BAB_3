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