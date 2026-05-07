class NodeGudang:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTreeGudang:
    def __init__(self):
        self.root = None

    def insert_root_manual(self, data):
        new_data = NodeGudang(data)
        if self.root is None:
            self.root = new_data
            return
        
    def insert_left_manual(self, parent_node, data):
        new_data = NodeGudang(data)
        if parent_node is None:
            parent_node.left = new_data
            return
        else:
            new_data.left = parent_node.left
            parent_node.left = new_data

    def insert_right_manual(self, parent_node, data):
        new_data = NodeGudang(data)
        if parent_node is None:
            parent_node.right = new_data
            return
        else:
            new_data.right = parent_node.right
            parent_node.right = new_data 

    def traverse_preorder(self, node):
        hasil = []
        if node is not None:
            print(node.data, end=" - ")
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

    def traverse_inorder(self, node):
        if node is not None:
            self.traverse_inorder(node.left)
            print(node.data, end=" - ")
            self.traverse_inorder(node.right)

    def traverse_postorder(self, node):
        if node is not None:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print(node.data, end=" - ")

    def get_leaf_nodes(self, data, leaf=""):
        if data is None:
            return leaf
        if data.left is None and data.right is None:
            if leaf :
                leaf += ", "
            leaf += str(data.data)
            return leaf
        
        leaf = self.get_leaf_nodes(data.left, leaf)
        leaf = self.get_leaf_nodes(data.right, leaf)
        
        return leaf 

data1 = BinaryTreeGudang()
data1.insert_root_manual("A")
data1.insert_left_manual(data1.root, "B")
data1.insert_right_manual(data1.root, "C")
data1.insert_left_manual(data1.root.left, "D")
data1.insert_right_manual(data1.root.left, "E")
data1.insert_right_manual(data1.root.right, "F")

print(f"""
SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"
======================================
[INFO] Membangun Struktur Gudang...
[INFO] Struktur berhasil dibuat.
""")

print("HASIL AUDIT:")
print("1. Pre-Order  : ", end="")
data1.traverse_preorder(data1.root)  
print("\n2. In-Order   : ", end="")
data1.traverse_inorder(data1.root) 
print("\n3. Post-Order : ", end="")
data1.traverse_postorder(data1.root)

print(f"""
[DATA] Gudang Ujung (Leaf Nodes) : {data1.get_leaf_nodes(data1.root)}
======================================
Audit Selesai!
""")
