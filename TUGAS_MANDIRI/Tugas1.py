import platform

daftar_buah = ["apel", "pisang", "semangka", "jeruk", "kiwi"]

print("Daftar buah :", daftar_buah)
print("Jumlah buah :", len(daftar_buah))

print("Buah pertama :", daftar_buah[0])
print("Buah ketiga :", daftar_buah[2])
print("Buah terakhir :", daftar_buah[-1])

print("Tiga buah pertama :", daftar_buah[:3])

daftar_buah.append("mangga")
daftar_buah.insert(2, "pepaya")

print("Setelah ditambah :", daftar_buah)

daftar_buah.remove("apel")

print("Setelah dihapus :", daftar_buah)

daftar_buah.sort()

print("Setelah diurutkan :", daftar_buah)

tuple_buah = tuple(daftar_buah)

print("Tuple buah :", tuple_buah)
print("Tipe data :", type(tuple_buah))

print("\nIsi tuple:")
for buah in tuple_buah:
    print(buah)

print("\nNama Komputer :", platform.node())