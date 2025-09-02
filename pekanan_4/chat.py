with open("survei.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]  # hapus baris kosong

survei_data = []
i = 0
while i < len(lines):
    if lines[i].startswith("pertanyaan:"):
        pertanyaan = lines[i].replace("pertanyaan:", "").strip()
        opsi = []
        if i+1 < len(lines) and lines[i+1].startswith("opsi:"):
            opsi = lines[i+1].replace("opsi:", "").strip().split(", ")
        survei_data.append({
            "pertanyaan": pertanyaan,
            "opsi": opsi
        })
    i += 1

# Inisialisasi hasil polling
hasil_polling = {}
for item in survei_data:
    for opsi in item["opsi"]:
        hasil_polling[opsi] = 0

# Jalankan polling
for item in survei_data:
    print(item["pertanyaan"])
    print("Pilihan:", ", ".join(item["opsi"]))
    while True:
        jawaban_user = input("Jawaban lu: ")
        if jawaban_user in item["opsi"]:
            print("---confirmed---\n")
            hasil_polling[jawaban_user] += 1
            break
        else:
            print("Masukin jawaban yg sesuai ama opsi!")

# Hasil akhir
total_suara = sum(hasil_polling.values())
print("\n=== HASIL POLLING ===")
for opsi, jumlah in hasil_polling.items():
    print(f"{opsi}: {jumlah} suara")
print("Total suara:", total_suara)