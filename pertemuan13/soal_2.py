"""
Latihan 2: Modifikasi List
    1. Gunakan list jadwal_senin dari latihan sebelumnya.
    2. Ternyata jam pelajaran "Olahraga" dipindah ke hari Selasa. Ubah elemen "Olahraga" menjadi
    "Kimia".
    3. Cetak list jadwal_senin yang sudah diperbarui.
"""

jadwal_senin = ["Matematika", "Bahasa Indonesia", "Olahraga", "Sejarah"]
print("\n---latihan 2----")
jadwal_senin[2] = "Kimia"
print(f"Jadwal baru =\n{jadwal_senin}")