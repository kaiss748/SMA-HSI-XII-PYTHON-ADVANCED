"""
Latihan 3: Analisis Kata
Buat program yang:
    1. Meminta pengguna memasukkan sebuah kalimat.
    2. Gunakan .split() untuk mengubah kalimat tersebut menjadi sebuah list kata-kata.
    3. Gunakan len() untuk menghitung dan mencetak jumlah kata dalam kalimat.
    4. Gunakan .sort() pada list tersebut untuk mengurutkan kata-kata berdasarkan abjad, lalu cetak
    list yang sudah terurut.
"""

print("\n---Latihan 3---")
kalimat = input("Masukin kalimat apapun: ")
list_kalimat = kalimat.split()
print(f"Jumlah elemen: {len(list_kalimat)}")
list_kalimat.sort()
print(list_kalimat)