"""
Latihan 4: Dictionary dengan Tuple Key
Buatlah sebuah dictionary bernama papan_catur. Gunakan tuple (baris, kolom) sebagai key
untuk menyimpan nama bidak catur. Contoh:
    papan_catur[(1, 'a')] = "Benteng Putih"
    papan_catur[(8, 'h')] = "Benteng Hitam"
Isi beberapa posisi, lalu akses dan cetak bidak yang ada di posisi (1, 'a').
"""

papan_catur = {
    (1, 'a'): "Benteng Putih",
    (8, 'h'): "Benteng Hitam",
    (8, 'g'): "Kuda Hitam",
    (1, 'd'): "Ratu Putih",
    (8, 'e'): "Raja Hideung",
    (8, 'f'): "Gajah Hitam",
    (1, 'g'): "Kuda Putih"
}

print(f"posisi catur (1, 'a'): {papan_catur[(1, 'a')]}")

# papan_catur[(1, 'a')] = "Benteng Putih"
# papan_catur[(8, 'h')] = "Benteng Hitam"
# papan_catur[(8, 'g')] = "Kuda Hitam"
# papan_catur[(1, 'd')] = "Ratu Putih"
# papan_catur[(8, 'e')] = "Raja Hideung"
# papan_catur[(8, 'f')] = "Gajah Hitam"
# papan_catur[(1, 'g')] = "Kuda Putih"
