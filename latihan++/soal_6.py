"""
Latihan 6: Validasi Input dengan while
Buat program yang meminta pengguna memasukkan umur mereka. Program harus terus meminta input
selama pengguna memasukkan nilai yang tidak valid (bukan angka atau angka di luar rentang wajar, misal <
0 atau > 100). Gunakan while True loop, try-except untuk menangani ValueError, dan if untuk
mengecek rentang. Jika input sudah valid, cetak umur tersebut dan hentikan loop dengan break.
"""


while True:
    try:
        umur = int(input("Masukkan umur Anda: "))
        if 100 >= umur >= 0:
            print(f"Thanks ur age is {umur}!")
            break
        else:
            print("nah dude umur lu ga make sanse_-")
            continue
    except ValueError:
        print("Invalid. cukup masukin angkanya aja bro!")
