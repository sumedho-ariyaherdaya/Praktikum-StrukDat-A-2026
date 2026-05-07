# BAGIAN A
class Node:
    def __init__(self, data_buku):
        self.next = None
        self.prev = None
        self.data_buku = data_buku

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_tail(self, data):
        new_node = Node(data)
    
        if self.head is None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr

    def print_forward(self):
        curr = self.head
        while curr:
            print(curr.data_buku, end=" <-> ")
            curr = curr.next
        print("None")

    def print_backward(self):
        curr = self.head

        while curr and curr.next:
            curr = curr.next

        while curr:
            print(curr.data_buku, end=" <-> ")
            curr = curr.prev
        print("None")
        
    def delete_by_judul(self, data):
        curr = self.head

        while curr:
            if curr.data_buku == data:
                if curr.prev is None:
                    self.head = curr.next
                    if self.head:
                        self.head.prev = None
                else:
                    curr.prev.next = curr.next

                    if curr.next:
                        curr.next.prev = curr.prev
                return
            curr = curr.next


dll = DoublyLinkedList()

dll.insert_tail("Laskar Pelangi")
dll.insert_tail("Bumi Manusia")
dll.insert_tail("Sang Pemimpi")

print("List Buku:")
dll.print_forward()
dll.print_backward()
dll.delete_by_judul("Bumi Manusia")
print("Setelah hapus Bumi Manusia:")
dll.print_forward()


                                                            