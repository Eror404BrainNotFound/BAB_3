import platform

print("=== BAGIAN A : DATA UKM ===")

ukm_ti = {"Budi", "Ani", "Citra", "Doni", "Eka"}
ukm_olahraga = {"Budi", "Ani", "Fani", "Gilang", "Hadi"}

print("Ikut keduanya :", ukm_ti.intersection(ukm_olahraga))

print("Seluruh peserta :", ukm_ti.union(ukm_olahraga))

print("Hanya UKM TI :", ukm_ti.difference(ukm_olahraga))

hadir = ["Budi", "Ani", "Budi", "Citra", "Ani", "Doni"]

peserta_unik = set(hadir)

print("Peserta unik hadir :", peserta_unik,
      "->", len(peserta_unik), "orang")

print("\n=== BAGIAN B : DATA MAHASISWA ===")

mahasiswa = {
    "nama": "Budi",
    "nim": "C030323001",
    "prodi": "Teknik Informatika",
    "hobi": ["Gaming", "Coding"]
}

print("\nKEYS")
for kunci in mahasiswa.keys():
    print(kunci)

print("\nVALUES")
for nilai in mahasiswa.values():
    print(nilai)

print("\nITEMS")
for k, v in mahasiswa.items():
    print(k, ":", v)

mahasiswa.update({
    "prodi": "Teknologi Informasi"
})

print("\nUpdate Prodi")
print(mahasiswa)

mahasiswa["hobi"].append("Membaca")

print("\nTambah Hobi")
print(mahasiswa)

mahasiswa["ipk"] = 3.85

print("\nTambah IPK")
print(mahasiswa)

mahasiswa.pop("nim")

print("\nHapus NIM")
print(mahasiswa)

if "nim" in mahasiswa:
    print("Kunci nim masih ada")
else:
    print("Kunci nim sudah tidak ada")

print("\nNama Komputer :", platform.node())