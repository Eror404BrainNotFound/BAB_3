import platform
import os

os.system('cls')

# Sampel-1
list1 = ["apel", "pisang", "semangka"]
list1.append("jeruk")
print(list1)

# Sampel-2
list2 = ["apel", "pisang", "semangka"]
list2.insert(1, "jeruk")
print(list2)

# Sampel-3
list3 = ["apel", "pisang", "semangka"]
listBaru = list3.copy()
print(listBaru)

# Sampel-4
list4 = [3, 5, 4, 9, 9, 2, 3, 2, 9]
print(list4.count(2))

print("Nama Komputer\t:", platform.node())