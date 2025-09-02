"""
Pertemuan 18: Pengenalan Objek
Latihan: "Resep Digital"
Buat sebuah class bernama Resep.

    1. __init__(self, nama_resep): Constructor ini harus menerima nama resep dan menginisialisasi
      dua atribut: self.nama_resep dan self.daftar_bahan (sebagai list kosong).
    2. tambah_bahan(self, bahan): Sebuah method yang menggunakan .append() untuk
      menambahkan bahan baru ke self.daftar_bahan.
    3. cetak_resep(self): Sebuah method yang mencetak nama resep, diikuti dengan daftar semua
      bahan yang sudah ditambahkan.
    4. Buat sebuah object resep_nasi_goreng dari class Resep, tambahkan beberapa bahan
      menggunakan method-nya, lalu cetak resep lengkapnya.
"""

class Resep:
    def __init__(self, nama_resep):
        self.nama_resep = nama_resep
        self.daftar_bahan = []
    def tambah_bahan(self, bahan):
        self.daftar_bahan.append(bahan)
    def cetak_resep(self):
        print(f"{self.nama_resep}")
        print(f"{self.daftar_bahan}")

resep_nasi_goreng = Resep("Nasgor gile")

resep_nasi_goreng.tambah_bahan("nasi")
resep_nasi_goreng.tambah_bahan("bawang")
resep_nasi_goreng.tambah_bahan("telur")
resep_nasi_goreng.cetak_resep()