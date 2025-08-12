file_input = "transaksi_kotor.txt"
file_output = "laporan_bersih.txt"

try:
    with open(file_input, 'r') as finput:
        with open(file_output, 'w') as foutput:
            foutput.write("LAPORAN TRANSAKSI BERSIH")
            foutput.write("\n=========================\n\n")
            for baris in finput:
                baris = baris.strip()
                data_potongan = baris.split(',')
                id_transaksi = data_potongan[0].strip(" ").upper()
                nama_produk = data_potongan[1].title()
                jumlah = int(data_potongan[2].strip(" "))
                harga_satuan = float(data_potongan[3].strip(" "))
                total_harga = jumlah * harga_satuan
                output_bersih = f"ID: {id_transaksi} | Produk: {nama_produk} | Jumlah: {jumlah} | Total Harga: {total_harga}\n"
                foutput.write(output_bersih)
            foutput.write("\n--- ANALISIS SELESAI ---.")


except FileNotFoundError:
    print("filenya kga ada boss_-")

print("Proses pembersihan data selesai. Laporan disimpan di laporan_bersih.txt")




