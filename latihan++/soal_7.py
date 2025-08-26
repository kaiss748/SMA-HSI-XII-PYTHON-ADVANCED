"""
Latihan 7: Pola Akumulator dengan while
Buat program untuk menghitung jumlah kuadrat dari N bilangan bulat pertama.
    1. Minta pengguna memasukkan sebuah angka N.
    2. Gunakan while loop untuk menghitung 1² + 2² + 3² + ... + N².
    3. Cetak hasil akhirnya.

Contoh Input: N = 3
Output yang diharapkan: Jumlah kuadrat dari 3 bilangan pertama adalah: 14 (karena 11 +
22 + 3*3 = 1 + 4 + 9 = 14).
"""

N = int(input("masukkan sebuah angka N: "))
angka = 1
jumlah = 0
while angka <= N:
    jumlah += angka**2
    angka += 1
print(f"Jumlah kuadrat dari {N} bilangan pertama adalah: {jumlah}")
