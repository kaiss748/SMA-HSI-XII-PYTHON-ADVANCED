"""
Latihan 1: Class Kucing
    1. Buatlah sebuah class bernama Kucing.
    2. Buat constructor __init__() yang menerima dua parameter: nama dan warna. Constructor ini
        harus menyimpan nilai-nilai tersebut ke dalam atribut self.nama dan self.warna.
    3. Buat sebuah method bernama bersuara() yang tidak memiliki parameter (selain self). Ketika
        dipanggil, method ini harus mencetak "Meow!".
    4. Buat sebuah method bernama perkenalkan_diri() yang mencetak kalimat seperti "Halo, saya
        kucing bernama [nama] dan warna saya [warna].".
    5. Buat dua object (instance) dari class Kucing dengan nama dan warna yang berbeda (misal, "Oren"
        berwarna "Oranye" dan "Milo" berwarna "Coklat").
    6. Panggil method perkenalkan_diri() dan bersuara() dari kedua objek tersebut.
"""

class Kucing:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def bersuara(self):
        print("Meow!")

    def perkenalan_diri(self):
        print(f"Halo, saya kucing bernama {self.nama} dan warna saya {self.warna}.")


Kucing_joana = Kucing("joana", "grey")
Kucing_hugo = Kucing("hugo", "golden brown")

Kucing_joana.bersuara()
Kucing_joana.perkenalan_diri()
Kucing_hugo.bersuara()
Kucing_hugo.perkenalan_diri()

        