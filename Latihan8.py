import platform
import os

os.system('cls')

# Sampel-1
tuple1 = ("apel", 34, True, 40, "pisang")
print(tuple1)

# Sampel-2
tuple2 = ("apel", "pisang", "semangka", "apel", "semangka")
print(tuple2)

# Sampel-3
tuple3 = ("apel", "pisang", "semangka")
print("Panjang tuple yaitu", len(tuple3))

for i in range(len(tuple3)):
    print(end=tuple3[i] + " ")
print()

# Sampel-4
tuple4 = ("apel", "pisang", "semangka")
print(type(tuple4))

# Sampel-5
tuple5 = tuple(("apel", "pisang", "semangka"))
print(tuple5)

print("Nama Komputer\t:", platform.node())