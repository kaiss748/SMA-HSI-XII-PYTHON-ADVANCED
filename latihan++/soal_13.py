"""
Latihan 13: Membangun String dengan Pola
Buat program yang meminta input sebuah kata dari pengguna. Program kemudian harus membangun
sebuah string baru berbentuk "piramida" dari kata tersebut.
    Gunakan for loop dengan range(len(kata)).
    Gunakan slicing kata[:i+1] untuk mendapatkan potongan kata di setiap iterasi.
Contoh Input: "Python"
Contoh Output:
P
Py
Pyt
Pyth
Pytho
Python
"""

kata = input("Masukin kata apa aja: ")
for i in range(len(kata)):
    i = kata[:i+1]
    # print(kata)
    print(i)

