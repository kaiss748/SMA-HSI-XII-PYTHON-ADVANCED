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


"""
Latihan 4: Memahami Aliasing
Prediksikan output dari kode di bawah ini sebelum menjalankannya. Jelaskan mengapa outputnya seperti
itu.
a = [1, 2, 3, 4, 5]
b = a
c = a.copy()
b[1] = 20
c[1] = 30
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
"""

"""
Jawaban: 
a = [1, 20, 2, 3, 4, 5]
b = [1, 20, 2, 3, 4, 5]
c = [1, 30, 2, 3, 4, 5]
Penjelasan:
ketika b dirubah maka a juga ikut terubah, karena merujuk ke objek yang sama,
dan address nya pun sama, sedang c itu membuat list baru, uda beda address
"""

print("\n---Latihan 4---")
a = [1, 2, 3, 4, 5]
b = a
c = a.copy()
b[1] = 20
c[1] = 30
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))