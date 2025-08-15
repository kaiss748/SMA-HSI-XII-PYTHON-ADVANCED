"""
Latihan 1: Iterasi dan Kalkulasi
Diberikan dictionary harga buah: harga_buah = {"apel": 5000, "jeruk": 8500, "mangga":
7800, "pisang": 3000}.
Gunakan for loop dan .items() untuk mencetak setiap buah dan harganya dalam format "Harga 1 kg
[nama buah] adalah Rp [harga]". Di akhir, hitung dan cetak total harga semua buah.
"""

harga_buah = {"apel": 5000,
              "jeruk": 8500, 
              "mangga": 7800,
              "pisang": 3000
}

data_item = harga_buah.items()
total = 0
for nama, harga in data_item:
    print(f"Harga 1 kg {nama} adalah Rp {harga:,.2f}")
    total += harga

print(f"total semua harga buah bray: Rp {total:,.2f}")