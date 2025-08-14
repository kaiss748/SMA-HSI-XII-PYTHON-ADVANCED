"""
Latihan 4: Slicing dan Penggabungan
    1. Buat dua buah list: awal_minggu = ["Senin", "Selasa", "Rabu"] dan akhir_minggu =
    ["Kamis", "Jumat", "Sabtu", "Minggu"].
    2. Gunakan operator + untuk menggabungkan keduanya menjadi list baru bernama seminggu.
    3. Dari list seminggu, gunakan slicing untuk membuat list baru bernama hari_kerja yang hanya
    berisi hari Senin sampai Jumat.
    4. Cetak list hari_kerja.
"""

print("\n---latihan 4----")
awal_pekan = ["Senin", "Selasa", "Rabu"]
akhir_pekan = ["Kamis", "Jumat", "Sabtu", "Minggu"]
sepekan = awal_pekan + akhir_pekan
hari_sibuk = sepekan[:5]
print(f"hari sibuk =\n{hari_sibuk}")