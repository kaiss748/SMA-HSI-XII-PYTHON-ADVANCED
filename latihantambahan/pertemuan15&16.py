"""
Pertemuan 15 & 16: Dictionary
Latihan: "Inventarisasi Barang"
Diberikan sebuah list yang berisi barang-barang yang baru datang ke gudang (dengan duplikat):
barang_datang = ["apel", "jeruk", "apel", "pisang", "apel", "jeruk"].
Tulis program yang mengubah list tersebut menjadi sebuah dictionary inventaris.
    1. Buat dictionary kosong inventaris.
    2. Gunakan for loop untuk setiap barang di barang_datang.
    3. Gunakan pola histogram (.get(barang, 0) + 1) untuk menghitung jumlah setiap barang.
    4. Cetak dictionary
"""

barang_datang = ["apel", "jeruk", "apel", "pisang", "apel", "jeruk"]

inventaris = {}

for barang in barang_datang:
    inventaris[barang] = inventaris.get(barang, 0) + 1
print(inventaris)