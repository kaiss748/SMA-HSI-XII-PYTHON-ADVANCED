"""
Pertemuan 11 & 12: Bekerja dengan Files
Latihan: "Filter Log File"
Buat sebuah file log.txt dengan isi berikut:

    INFO: Program dimulai.
    WARNING: Koneksi jaringan lambat.
    INFO: Data pengguna berhasil dimuat.
    ERROR: Gagal menulis ke database.
    INFO: Program selesai.

Buat program Python yang:
    1. Membaca file log.txt baris per baris.
    2. Menemukan semua baris yang mengandung kata "ERROR".
    3. Menulis hanya baris-baris yang mengandung "ERROR" ke file baru bernama error_log.txt.
    4. Setelah selesai, cetak pesan "Log error telah disaring ke error_log.txt".
"""

with open("log.txt", 'r') as file_handle:
    for baris in file_handle:
        if "ERROR" in baris:
            with open("error_log.txt", 'w') as file_error:
                file_error.write(baris)

