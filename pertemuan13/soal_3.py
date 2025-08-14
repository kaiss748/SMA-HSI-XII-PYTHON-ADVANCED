"""
Latihan 3: Traversing dan Modifikasi
    1. Buat sebuah list berisi angka: nilai_mentah = [55, 63, 72, 81, 90].
    2. Buatlah sebuah for loop yang menggunakan range(len(nilai_mentah)) untuk mengunjungi
setiap elemen.
    3. Di dalam loop, tambahkan 5 poin ke setiap nilai sebagai "nilai bonus".
    4. Setelah loop selesai, cetak list nilai_mentah yang sudah berisi nilai-nilai baru.
"""

print("\n---latihan 3----")
nilai_mentah = [55, 63, 72, 81, 90]
for i in range(len(nilai_mentah)):
    print(f"before -> {i}")
    # nilai_mentah[i] = nilai_mentah[i] + 2
    nilai_mentah[i] += 5
    print(nilai_mentah)
