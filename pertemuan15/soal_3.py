"""
Latihan 3: Penggunaan .get()
    1. Masih dengan dictionary biodata.
    2. Coba akses key "pekerjaan" menggunakan bracket notation []. Apa yang terjadi? (Beri komentar
pada baris ini agar tidak error).
    3. Sekarang, akses key "pekerjaan" menggunakan metode .get(). Cetak hasilnya.
    4. Akses lagi key
"""

biodata = {
    "nama": "kais",
    "umur": 18,
    "hobi":["membaca", "renang", "hangout"],
    "sudah_menikah": False
}

#print(biodata["pekerjaan"])  #error: keyerror: "pekerjaan"
pekerjaan = biodata.get("pekerjaan", "pelajar")
print(f"pekerjaan -> {pekerjaan}")
biodata["pekerjaan"] = "pelajar"
print(f"biodata update =\n{biodata}")