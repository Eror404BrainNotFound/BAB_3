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