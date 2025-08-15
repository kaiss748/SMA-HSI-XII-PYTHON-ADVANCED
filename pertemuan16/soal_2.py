"""
Latihan 2: Manajemen Kontak
Buat program manajemen kontak sederhana:
    1. Buat dictionary kosong bernama kontak.
    2. Tambahkan tiga kontak (misal: "Ibu", "Ayah", "Teman") beserta nomor teleponnya.
    3. Ubah nomor telepon "Ibu".
    4. Gunakan .pop() untuk menghapus "Teman".
    5. Cetak dictionary kontak akhir.
"""

kontak = {}
kontak["mama"] = "012345"
kontak["bapa"] = "014577"
kontak["vanni"] = "023891"
#mengubah kontak mama
kontak["mama"] = "098765"
nomor_vanni = kontak.pop("vanni")

print(f"kontak akhir nih =\n{kontak}")