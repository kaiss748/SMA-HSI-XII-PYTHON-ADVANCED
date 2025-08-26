"""
Latihan 15: Simulasi Password Lockout
Buat program login sederhana yang akan "mengunci" setelah 3 kali gagal.
    1. Buat variabel password_benar = "rahasia123" dan maks_percobaan = 3.
    2. Gunakan for loop dengan range(maks_percobaan).
    3. Di dalam loop, minta pengguna memasukkan password.
    4. Jika password benar, cetak "Login berhasil!" dan gunakan break untuk keluar dari loop.
    5. Jika salah, cetak pesan yang menunjukkan sisa percobaan.
    6. Gunakan else setelah for loop. Blok ini akan berjalan jika loop selesai tanpa break (artinya semua
percobaan gagal). Di dalamnya, cetak "Akun Anda terkunci!".
"""

password_benar = "rahasia123"
maks_percobaan = 3

for coba in range(maks_percobaan):
    passw = input("Masukkan Password: ")
    if passw == password_benar:
        print("Login berhasil!")
        break
    else:
        sisa = maks_percobaan - (coba+1)
        if sisa > 0:
            print(f"password anda salah | sisa percobaan: {sisa}")

else:
    print("Akun Anda terkunci!")
    

""" --- Cara ribet ---"""

password_benar = "rahasia123"
maks_percobaan = 3

for coba in range(maks_percobaan):
    passw = input("Masukkan Password: ")
    if passw == password_benar:
        print("Login berhasil!")
        break
    elif passw != password_benar:
        maks_percobaan -= 1
        print(f"Password lu salah | sisa percobaan: {maks_percobaan}")

    elif passw != password_benar:
        print(f"Password lu salah | sisa percobaan: {maks_percobaan}")

else:
    print("Akun Anda terkunci!")

