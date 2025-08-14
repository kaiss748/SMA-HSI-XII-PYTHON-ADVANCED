"""
Latihan 4: Memahami Aliasing
Prediksikan output dari kode di bawah ini sebelum menjalankannya. Jelaskan mengapa outputnya seperti
itu.
a = [1, 2, 3, 4, 5]
b = a
c = a.copy()
b[1] = 20
c[1] = 30
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
"""

"""
Jawaban: 
a = [1, 20, 2, 3, 4, 5]
b = [1, 20, 2, 3, 4, 5]
c = [1, 30, 2, 3, 4, 5]
Penjelasan:
ketika b dirubah maka a juga ikut terubah, karena merujuk ke objek yang sama,
dan address nya pun sama, sedang c itu membuat list baru, uda beda address
"""

print("\n---Latihan 4---")
a = [1, 2, 3, 4, 5]
b = a
c = a.copy()
b[1] = 20
c[1] = 30
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))