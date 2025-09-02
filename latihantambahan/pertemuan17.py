"""
Pertemuan 17: Tuples
Latihan: "Manajemen Koordinat Peta"
Bayangkan kamu membuat game sederhana. Kamu perlu menyimpan lokasi beberapa item penting di peta.
    1. Buat sebuah dictionary kosong bernama lokasi_item.
    2. Gunakan tuple (x, y) sebagai key untuk dictionary tersebut.
    3. Tambahkan beberapa item ke dictionary, contoh: lokasi_item[(10, 20)] = "Peti Harta
      Karun", lokasi_item[(5, 8)] = "Pohon Ajaib".
    4. Minta pengguna memasukkan koordinat X dan Y.
    5. Bentuk tuple dari input pengguna, lalu gunakan tuple tersebut untuk mengecek apakah ada item
      di lokasi_item. Cetak nama itemnya jika ada, atau "Tidak ada apa-apa di sini" jika tidak ada.
"""

lokasi_item = {}

lokasi_item[(10, 20)] = "Peti Harta Karun"
lokasi_item[(5, 8)] = "Pohon Ajaib"
x = int(input("masukan koordinat X: "))
y = int(input("masukan koordinat Y: "))

posisi = (x, y)

if posisi in lokasi_item:
    print(f"ada {lokasi_item[posisi]} di {posisi}!")
else:
    print("Tidak ada apa-apa di sini")
    