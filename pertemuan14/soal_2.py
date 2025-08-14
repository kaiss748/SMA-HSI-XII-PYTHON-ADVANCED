"""
Latihan 2: Mengurutkan Tanpa Mengubah
    1. Buat list nilai = [98, 76, 88, 100, 54].
    2. Gunakan fungsi sorted() untuk mendapatkan versi terurut dari list tersebut dan simpan di
    variabel baru.
    3. Cetak list nilai yang asli (pastikan ia tidak berubah).
    4. Cetak list baru yang sudah terurut.
"""

print("\n---Latihan 2---")
list_nilai = [98, 76, 88, 100, 54]
nilai_baru = sorted(list_nilai)
print(f"sebelum dirubah =\n{list_nilai}")
print(f"setelah dirubah =\n{nilai_baru}")