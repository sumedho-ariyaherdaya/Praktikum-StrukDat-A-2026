# BAGIAN B
class Node:
    def __init__(self, nama):
        self.next = None
        self.nama = nama

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, nama):
        new_node = Node(nama)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head

    def print_antrian(self):
        if self.head is None:
            print("linked list kosong")
            return
        
        curr = self.head

        while True:
            print(curr.nama, end=" -> ")
            curr = curr.next

            if curr == self.head:
                break

        print("(kembali ke head})")

    def delete_head(self, nama):
        if self.head is None:
            return

        curr = self.head
        prev = None

        while True:
            if curr.nama == nama:
                if curr == self.head and curr.next == self.head:
                    self.head = None
                    
                elif curr == self.head:
                    last = self.head
                    
                    while last.next != self.head:
                        last = last.next
                        
                    self.head = self.head.next
                    
                    last.next = self.head

                else:
                    prev.next = current.next

                return

            prev = current
            current = current.next

            if current == self.head:
                break
        
cll = CircularLinkedList()

cll.insert_tail("Andi")
cll.insert_tail("Budi")
cll.insert_tail("Citra")
cll.insert_tail("Dina")

print("List Nama:")
cll.print_antrian()

print("Nambah 'Edo'")
cll.insert_tail("Edo")
print("List Nama setelah ditambah:")
cll.print_antrian()
cll.delete_head("Andi")
print("Setelah dihapus:")
cll.print_antrian()

