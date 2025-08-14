try:
    with open("transaksi_kotor.txt", "r") as finput:
        with open("laporan_bersih.txt", "w") as foutput:
            foutput.write("LAPORAN TRANSAKSI BERSIH")
            foutput.write("\n=========================\n\n")

            grand_total = 0
            for baris in finput:
                baris = baris.strip()
                if not baris:
                    continue

                data_potongan = baris.split(',')
                id_transaksi = data_potongan[0].strip(" ").upper()
                nama_produk = data_potongan[1].strip(" ").title()
                jumlah = int(data_potongan[2].strip(" "))
                harga_satuan = float(data_potongan[3].strip(" "))
                total_harga = jumlah * harga_satuan
                    

                if total_harga > 500000:
                    output_bersih = f"ID: {id_transaksi} | Produk: {nama_produk} | Jumlah: {jumlah} | Total Harga: Rp {total_harga:,.2f}\n"
                    foutput.write(output_bersih)   
                    grand_total += total_harga

            foutput.write("\n--- ANALISIS SELESAI ---")
            foutput.write(f"\nTotal keseluruhan = Rp {grand_total:,.2f}")
    print("Proses pembersihan data selesai. Laporan disimpan di laporan_bersih.txt")

except FileNotFoundError:
    print("filenya kga ada boss_-")





