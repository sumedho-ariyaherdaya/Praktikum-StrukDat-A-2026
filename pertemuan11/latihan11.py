class Node:
    def __init__(self, nama_pasien, keluhan):
        self.nama_pasien = nama_pasien
        self.keluhan = keluhan
        self.next = None

class AntrianRumahSakit:
    def __init__(self):
        self.antrian_pertama = None # → head
        self.antrian_terakhir = None # → tail
        self.banyak_antrian = 0 # → size
        self.nomor_antrian_terakhir = 0 

    def is_antrian_kosong(self, cetak_pesan=False): # [IS_EMPTY]
        # Mengecek apakah antrian kosong
        cek_antrian = self.antrian_pertama is None

        # Syarat untuk mencetak pesan dibawah adalah memberikan argument cetak_pesan=True
        # Jadi pesan tidak akan tercetak otomatis
        if cetak_pesan:
            print("[CEK] Apakah antrian kosong?", end= " → ")
            if cek_antrian:
                print("YA, antrian masih kosong \n")
            else:
                print("Ada antrian")
        return cek_antrian
    
    def tambah_antrian(self, nama, keluhan): # [ENQUEUE]
        # Agar nomor antrian tetap lanjut meskipun sudah ada pasien yang dipanggil
        self.nomor_antrian_terakhir += 1

        # Menambah pasien ke dalam antrian
        antrian_baru = Node(nama, keluhan)
        # Jika antrian kosong, head dan tail akan diisi pasien baru
        if self.antrian_terakhir is None: 
            self.antrian_pertama = self.antrian_terakhir = antrian_baru 
        else:
            # Menyambungkan pasien terakhir saat ini ke pasien baru yang akan masuk
            self.antrian_terakhir.next = antrian_baru 
            # Memperbarui penanda 'antrian_terakhir' agar menunjuk ke pasien baru tersebut,
            # sehingga sistem tahu bahwa sekarang dia adalah orang terakhir di antrean.
            self.antrian_terakhir = antrian_baru 
        self.banyak_antrian += 1
        print(f'[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self.nomor_antrian_terakhir})')

    def panggil_antrian(self): # [DEQUEUE]
        # Mengecek apakah antrian kosong sebelum mengakses data
        if self.is_antrian_kosong():
            return "Antrian tidak ada: Tidak ada antrian untuk dipanggil"
        
        # Mengambil referensi ke pasien yang berada di posisi paling depan (yang akan dipanggil)
        antrian_sekarang = self.antrian_pertama
        # Menggeser pointer 'antrian_pertama' ke pasien berikutnya dalam antrean
        self.antrian_pertama = self.antrian_pertama.next

        # Jika setelag digeser pointer jadi None, maka antrian terakhir harus diset jadi None juga
        if self.antrian_pertama is None:
            self.antrian_terakhir = None
        
        self.banyak_antrian -= 1
        return f"[PANGGIL] Dokter memanggil: {antrian_sekarang.nama_pasien.upper()} (keluhan: {antrian_sekarang.keluhan})"

    def jumlah_antrian(self): # [SIZE]
        print(f"[INFO] Jumlah pasien menunggu: {self.banyak_antrian} orang")

    def lihat_antrian_pertama(self): # [PEEK]
         # Mengecek apakah antrian kosong sebelum mengakses data
        if self.is_antrian_kosong():
            return "Antrian kosong"
        return f"[PEEK] Pasien berikutnya: {self.antrian_pertama.nama_pasien.upper()} - {self.antrian_pertama.keluhan}"
    
    def tampilkan_semua_antrian(self):
        # Pointer sementara untuk menelusuri daftar antrean dari depan ke belakang
        daftar_antrian = self.antrian_pertama
        nomor = self.banyak_antrian
        while daftar_antrian:
            print("[ANTRIAN SAAT INI]")
            for i in range (nomor):
                print(f"  {i + 1}. {daftar_antrian.nama_pasien.ljust(7).upper()}   → {daftar_antrian.keluhan}")
                # Pindah ke node berikutnya (pasien selanjutnya)
                daftar_antrian = daftar_antrian.next
            
    
    def hapus_semua_antrian (self): # [CLEAR]
        # Reset semua penanda antrean ke titik awal (kosong)
        self.antrian_pertama = None
        self.antrian_terakhir = None
        self.banyak_antrian = 0
        self.nomor_antrian_terakhir = 0
        return f"[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan"

print("="*35)
print("     SISTEM ANTRIAN POLI UMUM")
print("     RS Sehat Bersama")
print("="*35)

pasien1 = AntrianRumahSakit()
# Mengecek apakah antrian kosong atau tidak [IS_EMPTY]
pasien1.is_antrian_kosong(cetak_pesan=True) #→ cetak_pesan = True agar pesan tercetak

# Menambahkan 3 pasien ke dalam antrian [ENQUEUE]
pasien1.tambah_antrian("Budi", "demam tinggi")
pasien1.tambah_antrian("Ani", "batuk pilek")
pasien1.tambah_antrian("Citra", "sakit kepala")
print(" ")

# Melihat jumlah pasien yang menunggu [SIZE]
pasien1.jumlah_antrian()

# Melihat pasien antrian pertama saat ini [PEEK]
print(pasien1.lihat_antrian_pertama()) 
print(" ")

# Memanggil pasien paling depan atau paling pertama menngantri [DEQUEUE]
print(pasien1.panggil_antrian())

# Menambah 1 pasien baru ke dalam antrian [ENQUEUE]
pasien1.tambah_antrian("Dodi", "nyeri perut")
print(" ")

# Menampilkan semua antrian saat ini
pasien1.tampilkan_semua_antrian()
print(" ")

# Memanggil pasien paling depan lagi [DEQUEUE]
print(pasien1.panggil_antrian())

# Melihat jumlah pasien yang menunggu [SIZE]
pasien1.jumlah_antrian()
print(" ")

# Menghapus semua antrian [CLEAR]
print(pasien1.hapus_semua_antrian())

# Mengecek apakah antrian kosong setelah semua antrian dihapus [IS_EMPTY]
if pasien1.is_antrian_kosong():
    print("[CEK] Apakah antrian kosong? → YA, antrian sudah kosong.")
print(" ")

print("="*35)
print("     Simulasi Selesai!")
print("="*35)