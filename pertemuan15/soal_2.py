"""
Latihan 2: Modifikasi Dictionary
    1. Gunakan dictionary biodata dari Latihan 1.
    2. Tambahkan pasangan key-value baru: "kota": "Nama Kotamu".
    3. Ubah value dari key "umur" menjadi umurmu tahun depan.
    4. Cetak dictionary yang sudah diperbarui.
"""

biodata = {
    "nama": "kais",
    "umur": 18,
    "hobi":["membaca", "renang", "hangout"],
    "sudah_menikah": False
}

biodata["kota"] = "San Vaganza"
biodata["umur"] = 19
print(f"upadated =\n{biodata}")