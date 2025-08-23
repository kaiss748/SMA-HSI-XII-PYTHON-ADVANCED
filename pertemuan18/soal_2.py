"""
Latihan 2: Class RekeningBank
Buatlah sebuah class bernama RekeningBank untuk mensimulasikan rekening bank sederhana.
    1. Buat constructor __init__() yang menerima dua parameter: nomor_rekening dan
        nama_pemilik. Ia juga harus menginisialisasi atribut self.saldo dengan nilai awal 0.
    2. Buat method lihat_saldo() yang mencetak saldo saat ini.
    3. Buat method setor(jumlah) yang menambahkan jumlah ke self.saldo dan mencetak pesan
        konfirmasi.
    4. Buat method tarik(jumlah) yang mengurangi jumlah dari self.saldo. Tambahkan logika if di
        dalamnya: jika jumlah yang ditarik lebih besar dari saldo, cetak pesan "Saldo tidak mencukupi" dan
        jangan ubah saldo. Jika tidak, kurangi saldo dan cetak pesan konfirmasi.
    5. Buat sebuah objek rekening_budi, lalu coba panggil semua method-nya: setor beberapa kali, tarik,
        dan lihat saldo.
"""

class RekeningBank:
    def __init__(self, nomor_rekening, nama_pemilik):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.jumlah_saldo = 0

    def lihat_saldo(self):
        print(f"saldo kau sekarang: Rp {self.jumlah_saldo:,.2f}")

    def setor(self, jumlah_setor):
        self.jumlah_saldo += jumlah_setor
        print(f"saldo berhasil ditambahkan ke {self.nomor_rekening} senilai: Rp {jumlah_setor:,.2f}")

    def tarik(self, jumlah_tarik):
        if jumlah_tarik > self.jumlah_saldo:
            print(f"Saldo kau ga cukup_-")
        else:
            self.jumlah_saldo -= jumlah_tarik
            print(f"Kau berhasil narik duet: Rp {jumlah_tarik:,.2f} dari rekening si {self.nama_pemilik}")


rekening_budie = RekeningBank("0203040506", "anthony budie")

rekening_budie.lihat_saldo()
rekening_budie.setor(200000)
rekening_budie.setor(170000)
rekening_budie.setor(50000)
rekening_budie.tarik(400000)
rekening_budie.lihat_saldo()

    

