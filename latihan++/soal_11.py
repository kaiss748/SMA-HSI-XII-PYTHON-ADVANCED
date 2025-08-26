"""
Latihan 11: Nested Loops untuk Pola Angka
Gunakan nested loops untuk menghasilkan pola angka berikut:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
Petunjuk: Loop luar mengontrol angka baris (1 sampai 5). Loop dalam mengontrol berapa kali angka
tersebut dicetak di baris itu.
"""

for i in range(1, 5+1, 1):
    for j in range(i):
        print(f"{i}", end=" ")
    print()