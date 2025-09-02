"""
Pertemuan 7 & 8: Iterasi / Loops
Latihan: "Tebak Angka (dengan Batasan Percobaan)"
Buat game tebak angka yang lebih menantang.

    1. Buat variabel angka_rahasia = 42 dan maks_percobaan = 5.
    2. Gunakan for loop dengan range(maks_percobaan) untuk memberi pengguna kesempatan
    terbatas.
    3. Di setiap iterasi, minta pengguna menebak angka.
    4. Beri petunjuk apakah tebakan mereka "Terlalu tinggi" atau "Terlalu rendah".
    5. Jika tebakan benar, cetak pesan kemenangan dan keluar dari loop dengan break.
    6. Gunakan else setelah for loop. Jika loop selesai tanpa break (artinya semua percobaan habis),
    cetak pesan "Game over! Anda kehabisan percobaan."
"""

angka_rahasia = 42
maks_percobaan = 5

for coba in range(maks_percobaan):
    passw = int(input("tebak angka rahasia: "))
    sisa = maks_percobaan - (coba+1)
    if passw > angka_rahasia:
        print(f"Terlalu tinggi | sisa percobaan: {sisa}")
        
    elif passw < angka_rahasia:
        print(f"Terlalu rendah | sisa percobaan: {sisa}")
        
    elif passw == angka_rahasia:
        print("anjayy, tebakan lu bener!!!")
        break
else:
    print("Game over! Anda kehabisan percobaan.")

    