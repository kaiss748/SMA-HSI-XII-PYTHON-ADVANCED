"""
Latihan 2: Validasi Nomor Telepon Sederhana
Buat program yang meminta pengguna memasukkan nomor telepon. Program harus memvalidasi apakah
input tersebut hanya berisi angka dan panjangnya antara 10 sampai 13 digit.
    - Gunakan re.search() dengan jangkar ^ dan $.
    - Gunakan quantifier + atau yang lebih spesifik.
    - Cetak "Format nomor telepon valid." atau "Format tidak valid."
    - Pola yang mungkin: ^\d+$ (ini hanya mengecek apakah semuanya digit, kamu perlu menambahkan
      pengecekan panjang dengan len()).
"""

import re
no_telp = input("masukin nomor bray: ")
pola = r'^\d+$'
match = re.search(pola, no_telp)

if match:
    if 10 <= len(no_telp) <= 13:
        if no_telp.startswith():
            print("Nice, no telp lu valid dude!")
            print(f"panjang no telp luh {len(no_telp)}")
        else:
            print("masukin no telpnya di awali 08")
    else:
        print("nah dude, no telp lu ga valid")
        print(f"panjang no telp luh {len(no_telp)}")
else:
    print("format salah, masukin nomer aja bray")

