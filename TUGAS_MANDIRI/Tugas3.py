import platform

data_mahasiswa = [
    {
        "nim": "C030323001",
        "nama": "Budi",
        "prodi": "TI",
        "nilai": [80, 75, 90]
    },
    {
        "nim": "C030323002",
        "nama": "Ani",
        "prodi": "TI",
        "nilai": [85, 88, 79]
    }
]

menu_sah = ("1", "2", "3", "4", "5", "6")


def tampilkan_data():
    print("\n=== DATA MAHASISWA ===")
    print("NIM\t\tNama\tProdi\tRata-rata")

    for mhs in data_mahasiswa:
        rata = sum(mhs["nilai"]) / len(mhs["nilai"])

        print(
            f"{mhs['nim']}\t{mhs['nama']}\t{mhs['prodi']}\t{rata:.2f}"
        )


def tambah_mahasiswa():
    nim = input("Masukkan NIM : ")

    for mhs in data_mahasiswa:
        if mhs["nim"] == nim:
            print("NIM sudah terdaftar")
            return

    nama = input("Masukkan Nama : ")
    prodi = input("Masukkan Prodi : ")

    nilai = []

    for i in range(1, 4):
        while True:
            try:
                n = float(input(f"Nilai ke-{i} : "))
                nilai.append(n)
                break
            except ValueError:
                print("Input harus berupa angka!")

    data_mahasiswa.append({
        "nim": nim,
        "nama": nama,
        "prodi": prodi,
        "nilai": nilai
    })

    print("Data berhasil ditambahkan")


def cari_mahasiswa():
    nim = input("Masukkan NIM yang dicari : ")

    for mhs in data_mahasiswa:
        if mhs["nim"] == nim:
            print("\nData ditemukan")
            for k, v in mhs.items():
                print(k, ":", v)
            return

    print("Data tidak ditemukan")


def mahasiswa_terbaik():
    terbaik = None
    rata_terbaik = 0

    for mhs in data_mahasiswa:
        rata = sum(mhs["nilai"]) / len(mhs["nilai"])

        if rata > rata_terbaik:
            rata_terbaik = rata
            terbaik = mhs

    print("\n=== MAHASISWA TERBAIK ===")
    print("NIM :", terbaik["nim"])
    print("Nama :", terbaik["nama"])
    print("Prodi :", terbaik["prodi"])
    print("Rata-rata :", round(rata_terbaik, 2))


def daftar_prodi():
    prodi_unik = set()

    for mhs in data_mahasiswa:
        prodi_unik.add(mhs["prodi"])

    print("\nDaftar Prodi :", prodi_unik)


while True:
    print("\n=== SISTEM PENDATAAN NILAI MAHASISWA ===")
    print("1. Tampilkan seluruh data")
    print("2. Tambah mahasiswa")
    print("3. Cari mahasiswa")
    print("4. Mahasiswa terbaik")
    print("5. Daftar prodi")
    print("6. Keluar")

    pilihan = input("Pilihan Anda : ")

    if pilihan not in menu_sah:
        print("Pilihan tidak valid")
        continue

    if pilihan == "1":
        tampilkan_data()

    elif pilihan == "2":
        tambah_mahasiswa()

    elif pilihan == "3":
        cari_mahasiswa()

    elif pilihan == "4":
        mahasiswa_terbaik()

    elif pilihan == "5":
        daftar_prodi()

    elif pilihan == "6":
        print("Program selesai")
        break

print("\nNama Komputer :", platform.node())