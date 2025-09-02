"""
Pertemuan 2: Program Pertama dan Ekspresi Matematika
Latihan: "Kalkulator Konversi Suhu"
Buat program yang mengonversi suhu dari Celsius ke Fahrenheit.
    1. Buat sebuah variabel, misalnya suhu_celsius, dan berikan nilai berupa angka (misal: 30).
    2. Gunakan rumus konversi: Fahrenheit = (Celsius * 9/5) + 32.
    3. Simpan hasil perhitungan ke dalam variabel baru bernama suhu_fahrenheit.
    4. Cetak hasilnya dalam format yang mudah dibaca, contoh: "30 derajat Celsius sama dengan
86.0 derajat Fahrenheit."
"""

suhu_celcius = 30
suhu_fahrenheit = (suhu_celcius * 9/5) + 32
print(f"{suhu_celcius} derajat Celcius sama dengan {suhu_fahrenheit} derajat Fahrenheit")