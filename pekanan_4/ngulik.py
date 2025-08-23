print("="*50)
tampilan_header = "WELCOME TO DRIFT SOCIETY".center(50, " ")
print(tampilan_header)
print("="*50+'\n')

SURVEI = [
    {
    "pertanyaan": "Pilih mobil yang bakal lu pake!",
    "opsi": ["GTR-R34", "GT-86", "Silvia-S15", "Mazda-RX7"]
    },
    {
    "pertanyaan": "Pilih mesin yang bakal lu pake!",
    "opsi": ["SR20DET", "2JZ", "V80"]
    },
    {
    "pertanyaan": "Siapa drifter favorit lu?",
    "opsi": ["Ziko Har", "Umbu Gil", "Vamella", "Dipo Dwi"]
    }
]

hasil_polling = {}
for item_survei in SURVEI:
    for opsi in item_survei["opsi"]:
        hasil_polling[opsi] = 0

for item_survei in SURVEI:
    print(item_survei["pertanyaan"])
    print(item_survei["opsi"])
    while True:
        jawaban = input("Jawaban lu: ")
        if jawaban in item_survei["opsi"]:
            print("Good choice\n")
            break
        else:
            print("nah bro masukin jawaban sesuai opsi")
    hasil_polling[jawaban] += 1

print("-"*50)
tampilan_closure = "UR POOLING RESULTS".center(50, " ")
print(tampilan_closure)
print("-"*50)

for opsi, jumlah in hasil_polling.items():
    print(f"{opsi}: {jumlah} suara")

print("="*50)
additional = "TQ FOR USING THIS PROGRAM BIG BRO!".center(50, " ")
print(additional)
print("="*50)