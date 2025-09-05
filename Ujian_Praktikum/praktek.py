try:
    with open("database_siswa.txt", 'r') as file:
        data_semua_siswa = {}
        
        for baris in file:
            bagian = baris.split(',')
            NIS = bagian[0]
            nama = bagian[1]
            nilai = bagian[2]
            nilai = [int(n) for n in nilai.split(';')] #memisahkan masing" nilai dan merubahnya menjadi int

            data_semua_siswa[NIS] = {
                'nama': nama,
                'nilai': nilai
            }
except FileNotFoundError:
    data_semua_siswa = {}

def lihat_daftar_siswa(data_siswa):
    if not data_siswa:
        print("Belum ada data siswa.")
    else:
        for nis, nama in data_siswa.items():
            print(f"{nis}: {nama['nama']}")

def lihat_detail_siswa(data_siswa):
    nis = input("masukan NIS siswa: ")
    if nis not in data_siswa:
        print("maaf, nomer NIS tidak ditemukan")
        return
    info = data_siswa[nis]
    nama = info['nama']
    nilai = info['nilai']

    print("\n--- Detail Siswa ---")
    print(f"NIS   : {nis}")
    print(f"Nama  : {nama}")
    print(f"Nilai : {nilai}")

    if nilai:
        rata_rata = sum(nilai) / len(nilai)
        tertinggi = max(nilai)
        terendah = min(nilai)

        if rata_rata >= 85:
            grade = 'A'
        elif rata_rata >= 75:
            grade = 'B'
        elif rata_rata >= 65:
            grade = 'C'
        elif rata_rata >= 50:
            grade = 'D'
        else:
            grade = 'E'

        print(f"Rata-rata : {rata_rata:.2f}")
        print(f"Tertinggi : {tertinggi}")
        print(f"Terendah  : {terendah}")
        print(f"Grade     : {grade}")
    else:
        print(f"Siswa belum memiliki nilai")

def tambah_siswa_baru(data_siswa):
    nis = input("masukan NIS siswa: ").strip()
    if nis in data_siswa:
        print("NIS sudah terdaftar")
        return
    else:
        nama = input("Masukan nama lengkap: ")

        data_semua_siswa[nis] = {
                'nama': nama,
                'nilai': []
            }
        print(f"Siswa baru dengan nama: {nama} dengan nis: {nis} berhasil ditambahkan!")
        return

def tambah_nilai_siswa(data_siswa):
    nis = input("masukan NIS siswa: ").strip()
    if nis not in data_siswa:
        print("maaf, nomer NIS tidak ditemukan")
        return
    
    nilai_input = input("masukkan nilai(jika lebih dari 1, pisahkan setiap angka dengan koma): ").strip()
    try:
        nilai_baru = [int(n) for n in nilai_input.split(',')]
    except ValueError:
        print("nilai harus berupa angka")
        return
    data_siswa[nis]['nilai'].extend(nilai_baru)
    print(f"Nilai: {nilai_baru} berhasil ditambahkan ke {data_siswa[nis]['nama']}")

def simpan_dan_keluar(data_siswa):
    with open("database_siswa.txt", 'w') as file:
        for nis, info in data_siswa.items():
            nilai = ";".join(str(n) for n in info['nilai'])
            baris = f"{nis},{info['nama']},{nilai}\n"
            file.write(baris)
    print("Data berhasil disimpan. Program berakhir.")
    exit()

while True:
    print("--- Sistem Informasi Siswa ---")
    print("1. Lihat Daftar Siswa")
    print("2. Lihat Detail Siswa")
    print("3. Tambah Siswa Baru")
    print("4. Tambah Nilai Siswa")
    print("5. Simpan & Keluar")
    print("-"*30)

    try:
        menu = int(input("Pilih menu: "))
    except ValueError:
        print("cukup masukkan angkanya")
        continue

    if menu == 1:
        lihat_daftar_siswa(data_semua_siswa)
    elif menu == 2:
        lihat_detail_siswa(data_semua_siswa)
    elif menu == 3:
        tambah_siswa_baru(data_semua_siswa)
    elif menu == 4:
        tambah_nilai_siswa(data_semua_siswa)
    elif menu == 5:
        simpan_dan_keluar(data_semua_siswa)
        break
    else:
        print("menu ga valid, pilih 1-5")







# with open("mbox-short.txt", 'r') as file:
#     pesan_mingguan = {}

#     for baris in file:
#         baris = baris.strip()
#         if baris.startswith("From "):
#             kata = baris.split()
#             hari = kata[2]

#             pesan_mingguan[hari] = pesan_mingguan.get(hari, 0) + 1
# print(f"dict :\n{pesan_mingguan}")
"""
output
dict :
{'Sat': 1, 'Fri': 20, 'Thu': 6}
"""