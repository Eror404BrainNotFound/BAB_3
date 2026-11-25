import platform
import os

os.system('cls')

# Sampel-1
list1 = ["apel", "pisang", "semangka", "jeruk", "kiwi", "melon", "mangga"]
print(list1[2:5])

# Sampel-2
list2 = ["apel", "pisang", "semangka", "jeruk", "kiwi", "melon", "mangga"]
print(list2[:4])

# Sampel-3
list3 = ["apel", "pisang", "semangka", "jeruk", "kiwi", "melon", "mangga"]
print(list3[2:])

# Sampel-4
list4 = ["apel", "pisang", "semangka", "jeruk", "kiwi", "melon", "mangga"]
print(list4[-4:-1])

print("Nama Komputer\t:", platform.node())