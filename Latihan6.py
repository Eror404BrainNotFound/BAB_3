import platform
import os

os.system('cls')

# Sampel-1
list1 = ["apel", "pisang", "semangka", "jeruk", "kiwi", "melon", "mangga"]
list1.remove("semangka")
print(list1)

# Sampel-2
list2 = ["apel", "pisang", "semangka", "jeruk", "kiwi", "melon", "mangga"]
list2.pop(1)
print(list2)

# Sampel-3
list3 = ["apel", "pisang", "semangka", "jeruk", "kiwi", "melon", "mangga"]
del list3[0]
print(list3)

# Sampel-4
list4 = ["apel", "pisang", "semangka", "jeruk", "kiwi", "melon", "mangga"]
list4.clear()
print(list4)

print("Nama Komputer\t:", platform.node())