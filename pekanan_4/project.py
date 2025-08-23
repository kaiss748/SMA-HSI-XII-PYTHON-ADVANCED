SURVEI = [
    {
        "pertanyaan": "Pilih bahasa pemrograman favoritmu bray!",
        "opsi": ["Python", "JavaScript", "Java", "C++"]
    },
    {
        "pertanyaan": "Apa sistem operasi yang paling sering lu pake?",
        "opsi": ["Windows", "macOS", "Linux"]
    },
    {
        "pertanyaan": "Tim mana yang akan menang di EPL musim ini?",
        "opsi": ["Liverpool", "LIVERPOOL", "LIVERpool", "liverPOOL"]
    }
]

print("="*50)
tampilan_header = "WELCOME TO THE BEST POOLING APP".center(50, " ")
print(tampilan_header)
print("="*50+'\n')

hasil_polling = {} 
for item_survei in SURVEI:
    for opsi in item_survei["opsi"]:
        hasil_polling[opsi] = 0

for item_survei in SURVEI:
    print(item_survei["pertanyaan"])
    print(item_survei["opsi"])
    while True:
        jawaban_user = input("Jawaban lu: ")
        if jawaban_user in item_survei["opsi"]:
            print(f"---confirmed---\n")
            break
        else:
            print("masukin jawaban yg sesuai ama opsi")
    
    hasil_polling[jawaban_user] += 1
total_suara = sum(hasil_polling.values())

print("-"*50)
tampilan_closure = "UR POOLING RESULTS".center(50, " ")
print(tampilan_closure)
print("-"*50)

for opsi, jumlah in hasil_polling.items():
    presentase = (jumlah / total_suara * 100) if total_suara > 0 else 0
    print(f"{opsi}: {jumlah} suara ({presentase:.2f}%)")

with open("hasil_polling.txt", 'w') as salin:
    salin.write("-"*50 + '\n')
    tampilan_salinan = "UR POOLING RESULTS".center(50, " ")
    salin.write(tampilan_salinan + '\n')
    salin.write("-"*50 + '\n')
    for opsi, jumlah in hasil_polling.items():
        presentase = (jumlah / total_suara * 100) if total_suara > 0 else 0
        salin.write(f"{opsi}: {jumlah} suara ({presentase:.2f}%)\n")
        

print("="*50)
additional = "TQ FOR USING THIS PROGRAM BIG BRO!".center(50, " ")
print(additional)
print("="*50)