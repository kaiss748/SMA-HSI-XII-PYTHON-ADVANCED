"""
Latihan 1: Membuat dan Mengakses
-. Buatlah sebuah list bernama jadwal_senin yang berisi nama-nama mata pelajaran hari Senin:
"Matematika", "Bahasa Indonesia", "Olahraga", "Sejarah".
    1. Cetak seluruh list.
    2. Cetak hanya mata pelajaran pertama.
    3. Cetak mata pelajaran terakhir menggunakan indeks negatif.
"""
print("---latihan 1----")
jadwal_senin = ["Matematika", "Bahasa Indonesia", "Olahraga", "Sejarah"]
print(f"jadwal hari senin =\n{jadwal_senin}")
print(f"matkul pertama -> {jadwal_senin[0]}")
print(f"matkul terakhir -> {jadwal_senin[-1]}")


"""
Latihan 2: Modifikasi List
    1. Gunakan list jadwal_senin dari latihan sebelumnya.
    2. Ternyata jam pelajaran "Olahraga" dipindah ke hari Selasa. Ubah elemen "Olahraga" menjadi
    "Kimia".
    3. Cetak list jadwal_senin yang sudah diperbarui.
"""

print("\n---latihan 2----")
jadwal_senin[2] = "Kimia"
print(f"Jadwal baru =\n{jadwal_senin}")


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