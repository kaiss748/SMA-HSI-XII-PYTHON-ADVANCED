"""
latihan 4: Histogram Kata
Buat program yang:
    1. Meminta pengguna memasukkan sebuah kalimat.
    2. Membuat histogram (dalam bentuk dictionary) yang menghitung frekuensi setiap kata (bukan
huruf) dalam kalimat tersebut.
    3. Cetak dictionary histogram tersebut.
Petunjuk: Gunakan metode .split() untuk mengubah kalimat menjadi list kata-kata terlebih
dahulu. Abaikan huruf besar/kecil dengan mengubah seluruh kalimat menjadi lowercase di awal.
"""

kalimat = input("masukin kalimat bray: ")
kalimat_input = kalimat.lower().split()
penghitung_kata = {}

for kata in kalimat_input:
    penghitung_kata[kata] = penghitung_kata.get(kata, 0) + 1

print(f"dict =\n{penghitung_kata}")
