def tambah_buku(nama, harga, stok):
    if harga > 0 and stok >= 0:
        return {"nama": nama, "harga": harga, "stok": stok}

    else:
        print("Error: Harga tidak valid")
        return None

data_buku = []
for i in range (3):
    nama = input("Masukkan Nama Buku:")
    harga = int(input("Masukkan Harga Buku:"))
    stok = int(input("Masukkan stok Buku:"))

    hasil = tambah_buku(nama, harga, stok)
    if hasil:
        data_buku.append(hasil)

print(data_buku)
