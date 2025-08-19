"""
Latihan 2: Immutability
Diberikan tuple koordinat_awal = (10, 20). Tulis kode yang menghasilkan tuple baru bernama
koordinat_baru yang nilainya (10, 25). Kamu tidak boleh mengubah koordinat_awal secara
langsung.
"""

koordinat_awal = (10, 20, 30, 40 ,50)
# koordinat_baru = (koordinat_awal[0], 25)
koordinat_baru = koordinat_awal[:1] + (25,) + koordinat_awal[2:]
# koordinat_baru = koordinat_awal[0] , ('25',) , koordinat_awal[2:]
print(koordinat_baru)
print(type(koordinat_baru))