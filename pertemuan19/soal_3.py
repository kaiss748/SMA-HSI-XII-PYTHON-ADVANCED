"""
Latihan 3: re.search() vs. re.findall()
Diberikan string teks = "python adalah bahasa yang menyenangkan, python mudah
dipelajari.".
    1. Gunakan re.search('python', teks). Apa yang dikembalikannya? Cetak .group()-nya.
    2. Gunakan re.findall('python', teks). Apa yang dikembalikannya? Cetak hasilnya.
    3. Jelaskan perbedaan output keduanya.
"""

import re
teks = "python adalah bahasa yang menyenangkan, python mudah dipelajari."
match = re.search('python', teks)
# match = match.group()
match1 = re.allfind('python', teks)

print(f"hasil 'search': {match.group()}")
print(f"hasil 'findall': {match1}")

"""
search: mengembalikan objek 'python' pertama dalam kalimat
findall: sesuai namanya, ia mengembalikan smua objek 'python' dalam kalimat
"""