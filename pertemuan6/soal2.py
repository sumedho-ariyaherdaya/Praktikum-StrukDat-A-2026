katalog = [
    {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
    {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
    ]

def cari_buku(katalog, keyword):
    hasil = [item for item in katalog if keyword.upper() in item['nama'].upper()]
    if hasil:
        return hasil
    else:
        print("Buku ini tidak ditemukan")
        return hasil
keyword = input("Cari Buku apa?")    
hasil_pencarian = cari_buku(katalog, keyword)

print(hasil_pencarian)