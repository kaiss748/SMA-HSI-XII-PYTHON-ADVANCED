"""
Latihan 10: for-else untuk Pengecekan Password
Simulasikan sebuah sistem yang mengecek apakah sebuah password mengandung karakter terlarang.
    1. Buat variabel password = "katasandi123" dan karakter_terlarang = "$%&".
    2. Gunakan for loop untuk memeriksa setiap karakter di password.
    3. Di dalam loop, gunakan if untuk mengecek apakah karakter tersebut ada di
karakter_terlarang. Jika ada, cetak "Password mengandung karakter terlarang!" dan gunakan
break.
    4. Gunakan blok else setelah for loop. Blok ini hanya akan berjalan jika break tidak pernah
dieksekusi, yang artinya password aman. Cetak "Password aman." di dalam else.
(Coba ubah password menjadi "kata$andi" dan lihat perbedaannya)
"""

# password = "kata$andi"
password = "katasandi123"
karakter_terlarang = "$%&"

for karakter in password:
    if karakter in karakter_terlarang:
        print("Password mengandung karakter terlarang!")
        break
else:
    print("Password aman.")