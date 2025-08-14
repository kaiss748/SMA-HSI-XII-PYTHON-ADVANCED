"""
Latihan 1: Membuat dan Mengakses
    1. Buat sebuah dictionary bernama biodata untuk merepresentasikan dirimu. Isinya harus memiliki
key: "nama", "umur", "hobi" (hobi bisa berupa list dari beberapa string), dan
"sudah_menikah" (berisi boolean).
    2. Cetak seluruh dictionary.
    3. Cetak hanya value dari key "nama".
    4. Cetak hobi pertamamu dari list hobi.
"""

biodata = {
    "nama": "kais",
    "umur": 18,
    "hobi":["membaca", "renang", "hangout"],
    "sudah_menikah": False
}

print(f"biodata -> {biodata}")
nama_oe = biodata["nama"]
print(f"nama saya -> {nama_oe}")
hobi_1 = biodata["hobi"][0]
print(f"hobi pertama -> {hobi_1}")