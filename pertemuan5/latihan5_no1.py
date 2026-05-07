stok_barang = [15, 40, 30, 10, 25]

stok_barang.pop(3)
stok_barang.insert(3, 50)
print("Nilai 10 diubah menjadi: ", stok_barang)

stok_barang.insert(0, 5)
stok_barang.sort
print("Nilai setelah diurutkan dan ditambah 5: ", stok_barang)

rata_rata = sum(stok_barang)/len(stok_barang)
print("Stok Aman") if rata_rata > 20 else print("Waspada")  
