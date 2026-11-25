import platform
import os

os.system('cls')

# Sampel-1
list1 = ["apel", "pisang", "semangka"]
list1[1] = "buah naga"
print(list1)

# Sampel-2
list2 = ["apel", "pisang", "semangka", "jeruk", "kiwi", "melon", "mangga"]
list2[1:3] = ["buah naga", "pepaya"]
print(list2)

# Sampel-3
list3 = ["apel", "pisang", "semangka"]
list3[1:2] = ["buah naga", "pepaya"]
print(list3)

# Sampel-4
list4 = ["apel", "pisang", "semangka"]
list4[1:3] = ["buah naga"]
print(list4)

print("Nama Komputer\t:", platform.node())