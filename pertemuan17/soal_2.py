"""
Latihan 2: Immutability
Diberikan tuple koordinat_awal = (10, 20). Tulis kode yang menghasilkan tuple baru bernama
koordinat_baru yang nilainya (10, 25). Kamu tidak boleh mengubah koordinat_awal secara
langsung.
"""

koordinat_awal = (10, 20)
koordinat_baru = (koordinat_awal[0], 25)
print(koordinat_baru)
print(type(koordinat_baru))