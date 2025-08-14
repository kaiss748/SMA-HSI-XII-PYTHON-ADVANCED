"""
Latihan 1: Manajemen Daftar Belanja
    1. Buat sebuah list kosong bernama belanjaan.
    2. Gunakan .append() untuk menambahkan "Telur", "Susu", dan "Roti".
    3. Gunakan .insert() untuk menambahkan "Apel" di posisi paling awal.
    4. Gunakan .remove() untuk menghapus "Susu".
    5. Cetak list akhir.
"""

print("---Latihan 1---")
belanjaan = []
belanjaan.append("Telur")
belanjaan.append("Susu")
belanjaan.append("Roti")
belanjaan.insert(0, "Apel")
belanjaan.remove("Susu")
print(f"Belanjaan luh =\n{belanjaan}")