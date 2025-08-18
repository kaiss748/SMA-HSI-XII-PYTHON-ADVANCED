"""
Latihan 3: Nested Dictionary
Buatlah sebuah nested dictionary untuk menyimpan data dua produk di sebuah toko online.
Key utamanya adalah ID produk (misal: "PROD001", "PROD002").
Setiap produk harus memiliki key untuk "nama", "harga", dan "stok".
Setelah membuatnya, tulis kode untuk mencetak nama dan harga dari produk dengan ID "PROD002".
"""

daftar_product = {
    "PROD001":{
        "nama": "obat kuat",
        "harga": 23000,
        "stok": 25
    },

    "PROD002":{
        "nama": "salonpas",
        "harga": 14000,
        "stok": 12
    }
}

prod2 = daftar_product["PROD002"]
print(f"nama = {prod2["nama"]}")
print(f"harga = Rp {prod2["harga"]:,.2f}")
print(f"stok = {prod2["stok"]}")