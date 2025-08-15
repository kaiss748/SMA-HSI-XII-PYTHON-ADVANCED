"""
Latihan 4: Frekuensi Hari
Tulis program yang membaca file mbox-short.txt. Bangun histogram menggunakan dictionary untuk
menghitung berapa banyak pesan yang dikirim pada setiap hari dalam seminggu. (Lihat baris yang dimulai
dengan "From ", kata ketiganya adalah hari). Cetak dictionary hasilnya.
"""

with open("mbox-short.txt", 'r') as file:
    pesan_mingguan = {}

    for baris in file:
        baris = baris.strip()
        if baris.startswith("From "):
            kata = baris.split()
            hari = kata[2]

            pesan_mingguan[hari] = pesan_mingguan.get(hari, 0) + 1
print(f"dict =\n{pesan_mingguan}")
        
