katalog = [
{'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
{'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]
riwayat = set()
def proses_transaksi(katalog, nama_buku, jumlah_beli):
    hasil = [item for item in katalog if nama_buku.upper() in item['nama'].upper() and item['stok'] > 0]
    if hasil:
        buku = hasil[0]
        if buku['stok'] >= jumlah_beli:
            buku['stok'] -= jumlah_beli
            harga = buku['harga'] * jumlah_beli
            print(harga)
            riwayat.add(buku['nama'])
        else: 
            print("Maaf, stok habis")
    else:
        print("Buku tak de la")

proses_transaksi(katalog, "Belajar Python", 2)
proses_transaksi(katalog, "Struktur Data", 5) # Stok kurang
proses_transaksi(katalog, "Belajar Python", 1)
print(riwayat)