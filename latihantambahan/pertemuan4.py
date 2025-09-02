"""
Pertemuan 4: Logika & Kondisi (if, else, elif, operator logika)
Latihan: "Kalkulator Diskon Wahana Bermain"
Buat program untuk menentukan harga tiket masuk wahana bermain berdasarkan usia dan hari kunjungan.
    1. Minta input usia (integer) dan hari_kunjungan (string, misal: "senin", "sabtu").
    2. Harga normal tiket adalah Rp 75.000.
    3. Terapkan aturan diskon berikut menggunakan if-elif-else:
        Jika usia di bawah 5 tahun atau di atas 60 tahun, diskon 50%.
        Jika bukan keduanya, tetapi berkunjung di hari kerja ("senin" sampai "jumat"), diskon 20%.
        Selain itu (usia normal di akhir pekan), tidak ada diskon.
    4. Cetak harga tiket akhir yang harus dibayar.
"""

usia = int(input("Halo dek, berapa usia mu: "))
hari_kunjungan = input("hari kunjugan: ")
hari_kunjungan = hari_kunjungan.lower()
harga_normal = 75000

if 5 > usia or 60 < usia:
    diskon = 50
elif hari_kunjungan != "sabtu" and hari_kunjungan != "minggu":
    diskon = 20
else:
    diskon = 0

total_diskon = harga_normal * diskon / 100
harga_tiket = harga_normal - total_diskon

print(f"Harga tiket yang harus kamu bayar Rp {harga_tiket:,.2f}")