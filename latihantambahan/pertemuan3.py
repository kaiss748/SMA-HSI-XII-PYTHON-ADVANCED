"""
Pertemuan 3: Variabel dan Tipe Data Dasar (str, int, float)
Latihan: "Kalkulator Sederhana Biaya Perjalanan"
Buat program interaktif yang menghitung perkiraan biaya bensin untuk sebuah perjalanan.
    1. Minta pengguna memasukkan tiga hal:
        Jarak perjalanan dalam kilometer (bisa desimal).
        Konsumsi bahan bakar mobil (km per liter, bisa desimal).
        Harga bensin per liter.
    2. Lakukan konversi tipe data yang sesuai untuk setiap input.
    3. Hitung berapa liter bensin yang dibutuhkan (jarak / konsumsi).
    4. Hitung total biaya perjalanan (liter_bensin * harga_per_liter).
    5. Cetak hasilnya dengan format yang jelas, contoh: "Untuk perjalanan 150.5 km, Anda
membutuhkan 12.54 liter bensin dengan total biaya Rp 188125.0"
"""

Jarak = float(input("Seberapa jauh perjalanan lu(km)? "))
Konsumsi = float(input("Berapa km per liter? "))
harga = int(input("Berapa harga bensin per liter? "))

liter_bensin = Jarak/Konsumsi
total_biaya = liter_bensin * harga

print(f"Buat perjalanan {Jarak} km, Lu butuh at least {liter_bensin} liter bensin dengan total biaya Rp {total_biaya:,.2f}")
