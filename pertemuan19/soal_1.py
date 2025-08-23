"""
Latihan 1: Temukan Semua Angka
Diberikan string: data = "Pendapatan bulan ini adalah Rp 1,500,000, sedangkan
pengeluaran sebesar Rp 850,000.".
Gunakan re.findall() untuk mengekstrak semua urutan angka dari string tersebut. Output yang
diharapkan adalah ['1', '500', '000', '850', '000'].
"""

import re
data = "Pendapatan bulan ini adalah Rp 1,500,000, sedangkan pengeluaran sebesar Rp 850,000."
pola = r'\d+'

hasil = re.findall(pola, data)
print(hasil)
