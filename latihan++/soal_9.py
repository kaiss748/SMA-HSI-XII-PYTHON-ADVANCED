"""
Latihan 9: Mencari Bilangan Prima Pertama
Buat program untuk menemukan dan mencetak 5 bilangan prima pertama setelah angka 1. Bilangan prima
adalah bilangan yang hanya bisa dibagi oleh 1 dan dirinya sendiri.
    1. Gunakan while loop luar untuk memastikan kamu sudah menemukan 5 bilangan prima.
    2. Gunakan for loop di dalamnya untuk mengecek apakah sebuah angka bisa dibagi oleh angka lain
        selain 1 dan dirinya sendiri.
    3. Kamu akan butuh sebuah "flag" (variabel boolean) untuk menandai apakah sebuah angka prima atau
tidak.
Output yang diharapkan:
2
3
5
7
11
"""

jumlah_prima = 0   # ->untuk menghitung brp banyak bilangan prima yg ditemukan
angka = 2 # ->start dari angka 2... karena angka 1 bukan prima

while jumlah_prima < 5:

    prima = True

    for i in range(2, angka):
        if angka % 2 == 0:
            prima = False
            break
        
    if prima:
            print(angka)
            jumlah_prima +=1
    angka += 1

