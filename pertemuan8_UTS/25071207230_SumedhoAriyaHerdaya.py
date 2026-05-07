#=== Soal 1 ===
pengunjung_hari_ini = [ 
{"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi",   
"kembali": False}, 
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",   
"kembali": True}, 
{"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi",   
"kembali": False}, 
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",   
"kembali": True}, 
{"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains",   
"kembali": False}, 
{"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum",   
"kembali": False}, 
]

def tampilkan_pengunjung():
    print("===== DATA PENGUNJUNG PERPUSTAKAAN ====")
    print("No |", "ID    |" , "Nama     |" , "Usia |" , "Kategori |" , "Status Kembali")
    n = len(pengunjung_hari_ini)
    for i in range (n):
        print(f"{i+1}  |", f"{pengunjung_hari_ini[i]["id"]}  |", f"{pengunjung_hari_ini[i]["nama"].ljust(6)}   |", f"{pengunjung_hari_ini[i]["usia"]}   |", f"{pengunjung_hari_ini[i]["kategori"].ljust(6)}   |", f"{pengunjung_hari_ini[i]["kembali"]}   ")

def filter_belum_kembali():
    belum_mengembalikan = [peminjam for peminjam in pengunjung_hari_ini if peminjam["kembali"] == False]
    n = len(belum_mengembalikan)
    nama_belum_mengembalikan = []
    for i in range (n):
        min_idx = i
        for j in range (i + 1, n):
            if belum_mengembalikan[j]["nama"] < belum_mengembalikan[min_idx]["nama"]:
                min_idx = j
                belum_mengembalikan[i], belum_mengembalikan[min_idx] = belum_mengembalikan[min_idx], belum_mengembalikan[i]
        nama = belum_mengembalikan[i]["nama"]
        nama_belum_mengembalikan.append(nama)
    
    print("===== PENGUNJUNG BELUM KEMBALI ====")
    
    for i in nama_belum_mengembalikan:
        print(f"{i}")
    total_belum_mengembalikan = len(belum_mengembalikan)
    
    print("Total belum kembali:", total_belum_mengembalikan)
print("=== SOAL 1 ===")
tampilkan_pengunjung()
filter_belum_kembali()

#=== Soal 2 ===
def info_perpustakaan():
    info_perpus = ("Nama: Perpustakaan Kampus Terpadu", "Alamat: Jl. Pendidikan No. 5, Pekanbaru", "Telp: 0761-54321 ")
    for i in info_perpus:
        print (i)

def rekap_kategori():
    kategori_buku = [buku["kategori"] for buku in pengunjung_hari_ini]
    buku_unik = set(kategori_buku)
    jumlah_buku_unik = len(buku_unik)
    print(f"Kategori Buku Unik: {buku_unik}")
    print(f"Jumlah Kategori: {jumlah_buku_unik}")

    pengunjung_buku_fiksi = 0
    pengunjung_buku_sains = 0
    pengunjung_buku_hukum = 0

    for i in pengunjung_hari_ini:
        if i["kategori"] == "Fiksi":
            pengunjung_buku_fiksi += 1
        if i["kategori"] == "Sains":
            pengunjung_buku_sains += 1
        if i["kategori"] == "Hukum":
            pengunjung_buku_hukum += 1
    print("Rekap per kategori:")
    print(f"Fiksi: {pengunjung_buku_fiksi} pengunjung")
    print(f"Sains: {pengunjung_buku_sains} pengunjung")
    print(f"Hukum: {pengunjung_buku_hukum} pengunjung")

    kategori_pengunjung_terbanyak = ""
    if pengunjung_buku_fiksi > pengunjung_buku_hukum and pengunjung_buku_fiksi > pengunjung_buku_sains:
        kategori_pengunjung_terbanyak = "Fiksi"
    elif pengunjung_buku_sains > pengunjung_buku_hukum and pengunjung_buku_sains > pengunjung_buku_fiksi:
        kategori_pengunjung_terbanyak = "Sains"
    elif pengunjung_buku_hukum > pengunjung_buku_fiksi  and pengunjung_buku_hukum > pengunjung_buku_sains:
        kategori_pengunjung_terbanyak = "Hukum"
    else:
        kategori_pengunjung_terbanyak = "Fiksi", "Sains", "Hukum"
    print(f"Kategori terbanyak:{kategori_pengunjung_terbanyak} (2 pengunjung)", )

print("=== SOAL 2 ===")
info_perpustakaan()
rekap_kategori()


#=== Soal 3 ===
class Pengunjung:
    total_pengunjung = 0
    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.total_pengunjung += 1

    def get_nama(self):
        return self.__nama
    
    def get_id(self):
        return self.__id
    
    def get_kategori(self):
        return self.__kategori
    
    def tampilkan_info(self):
        print(f"ID: {self.get_id()} | Nama: {self.get_nama()} | Kategori: {self.get_kategori()}")
    
    @staticmethod
    def hitung_pengunjung():
        print(f"Total Pengunjung Terdaftar: {Pengunjung.total_pengunjung}")

class PengunjungPrioritas(Pengunjung):
    def __init__(self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"ID: {self.get_id()} | Nama: {self.get_nama()} | Kategori: {self.get_kategori()} |  Prioritas: {self.prioritas}")
        if self.prioritas == "Mendesak":
            print("** Layani segera! **")

print("=== SOAL 3 ===")
p1 = Pengunjung("M001", "Rina", "Fiksi")
p2 = PengunjungPrioritas("M007", "Gilang", "Referensi", "Mendesak")
p1.tampilkan_info()
p2.tampilkan_info()
p2.hitung_pengunjung()


#=== Soal 4 ===
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class AntrianPeminjaman:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        pengunjung_baru = Node(data)
        if not self.head:
            self.head = pengunjung_baru
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = pengunjung_baru

    def tampilkan_antrean(self):
        curr = self.head
        while curr:
            print(f"{curr.data["id"]}  -", f"{curr.data["nama"].ljust(6)}   |",f"{curr.data["kategori"]}")
            curr = curr.next
 

print ("=== ANTRIAN PEMINJAMAN ===")
antrian = AntrianPeminjaman() 
antrian.tambah({"id": "M001", "nama": "Rina",   "kategori": "Fiksi"}) 
antrian.tambah({"id": "M002", "nama": "Hendra", "kategori": "Sains"}) 
antrian.tambah({"id": "M003", "nama": "Siti",   "kategori": "Fiksi"}) 
antrian.tambah({"id": "M004", "nama": "Taufik", "kategori": "Hukum"}) 
 
antrian.tampilkan_antrean()