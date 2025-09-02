"""
Pertemuan 13 & 14: List (Daftar)
Latihan: "Manajemen Daftar Tugas (To-Do List)"
Buat aplikasi to-do list interaktif sederhana.
    1. Buat sebuah list kosong bernama tugas.
    2. Gunakan while True loop sebagai menu utama.
    3. Minta input dari pengguna: "Apa yang ingin Anda lakukan? (tambah, hapus, lihat, keluar)".
    4. Gunakan if-elif-else:
        Jika "tambah", minta input tugas baru dan .append() ke list.
        Jika "lihat", cetak semua tugas dalam list dengan nomor urut.
        Jika "hapus", minta nomor tugas yang ingin dihapus, lalu .pop() dari list.
        Jika "keluar", gunakan break untuk menghentikan program.
"""

tugas = []

while True:
    opsi = input("Apa yang ingin Anda lakukan? (tambah, hapus, lihat, keluar): ")
    if opsi == "tambah":
        tugas_baru = input("masukan tugas baru: ")
        tugas_baru = tugas.append(tugas_baru)
    elif opsi == "lihat":
        if not tugas:
            print("blom ada tugas")
        else:
            print("\nDaftar tugas:")
            for i, tugas_baru in enumerate(tugas, start=1):
                print(f"{i}. {tugas_baru}")
    elif opsi == "hapus":
        nomor = int(input("nomor tugas yang ingin dihapus: "))
        tugas_dihapus = tugas.pop(nomor-1)
    elif opsi == "keluar":
        break