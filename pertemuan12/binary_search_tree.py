class NodePerpusatakaan:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BstPerpustakaan:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        buku_baru = NodePerpusatakaan(id_buku, judul)
        if self.root is None:
            self.root = buku_baru
            print(f"[INSERT] Berhasil memasukkan: ID {buku_baru.id_buku} - {buku_baru.judul}") 
            return
        
        A = self.root
        B = self.root

        while B is not None and buku_baru.id_buku != A.id_buku:
            A = B

            if buku_baru.id_buku < A.id_buku:    
                B = A.left
            else:
                B = A.right
             

        if buku_baru.id_buku == A.id_buku:
            print("ID Sama!")
            return

        if buku_baru.id_buku < A.id_buku:
            A.left = buku_baru 
        else:
            A.right = buku_baru
        
        print(f"[INSERT] Berhasil memasukkan: ID {buku_baru.id_buku} - {buku_baru.judul}") 
        

    def traversal_inorder(self, node, nomor=1):
        if node is not None:
            nomor = self.traversal_inorder(node.left, nomor)
            print(f"{nomor}.",node.id_buku, " - ", node.judul)
            nomor += 1
            nomor = self.traversal_inorder(node.right, nomor)
        return nomor
    
    def search(self, id_buku):
        cari_buku = self.root

        while cari_buku is not None:
            if id_buku == cari_buku.id_buku:
                print(f"[SEARCH] Mencari ID {id_buku}... Ditemukan! Judul: {cari_buku.judul}")
                return cari_buku
            elif id_buku < cari_buku.id_buku:
                cari_buku = cari_buku.left
            elif id_buku > cari_buku.id_buku:
                cari_buku = cari_buku.right
        print(f"[SEARCH] Mencari ID {id_buku}... Tidak ditemukan!")
        return cari_buku
    
    def get_min(self):
        id_terkecil = self.root

        while id_terkecil.left is not None:
            id_terkecil = id_terkecil.left

        return f"[STATISTIK] ID Terkecil: {id_terkecil.id_buku}"

    def get_max(self):
        id_terbesar = self.root

        while id_terbesar.right is not None:
            id_terbesar = id_terbesar.right

        return f"[STATISTIK] ID Terbesar: {id_terbesar.id_buku}"
    
    def height(self, node, ):
       if node is None:
        return -1
       
       left_height = self.height(node.left)
       right_height = self.height(node.right)
       return 1 + max(left_height, right_height)
   

print(f"""\n
SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"
=========================================
""")
data_buku = BstPerpustakaan()
data_buku.insert(50, "Dasar Pemrograman")
data_buku.insert(30, "Struktur Data")
data_buku.insert(70, "Kecerdasan Buatan")
data_buku.insert(20, "Matematika Diskrit")
data_buku.insert(40, "Basis Data")
data_buku.insert(60, "Jaringan Komputer")
data_buku.insert(80, "Sistem Operasi\n")

print("[INFO] Koleksi Buku (In-Order Traversal):")
data_buku.traversal_inorder(data_buku.root)

data_buku.search(60)
data_buku.search(100)

print("")
print(data_buku.get_min())
print(data_buku.get_max())
print(f"[INFO] Tinggi (Height) Tree: {data_buku.height(data_buku.root)}")

print(f"""
=========================================
Simulasi Selesai!
""")