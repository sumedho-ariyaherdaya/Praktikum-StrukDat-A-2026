# Bagian 1: Implementasi Menggunakan List Biasa
class StackList:
    def __init__(self):
        self.items = [] 

    def is_empty(self):
        print("Is Empty:", self.items == 0)
        return len(self.items) == 0

    def push(self, url):
        self.items.append(url)
        print("Push link:", self.items)

    def pop(self):
        if not self.is_empty():
            item_dihapus = self.items.pop()
            print("Pop link:", self.items)
            return item_dihapus
        raise IndexError("Riwayat kosong")
    
    def peek(self):
        if not self.is_empty():
            lihat_item = self.items[-1]
            print("Peek link:", lihat_item)
            return lihat_item
        else:
            return None
        
    def size(self):
        print("Size:", len(self.items))
        return len(self.items)
   
print("=== BAGIAN 1 ===")   
x = StackList()
x.is_empty()
x.push("google.com")
x.push("youtube.com")
x.push("youtube.music.com")
x.peek()
x.size()
x.pop()
x.peek()
x.size()
x.push("spotify.com")

# Bagian 2: Implementasi Menggunakan Linked List
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 

    def is_empty(self):
        print("Is Empty:", self.count == 0)
        return self.count == 0
    
    def push(self, url):
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1
        
    def pop(self):
        if self.is_empty():
            return "Riwayat Kosong"
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.url

    def peek(self):
        if self.is_empty():
            return "Riwayat Kosong"
        return self.top.url
    
    def size(self):
        print("Size:", self.count)
        return self.count
    
    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url, end=" -> ")
            currentNode = currentNode.next
        print()
    
print(" ")   
print("=== BAGIAN 2 ===")   
x1 = StackLinkedList()
x1.is_empty()
x1.push("google.com")
x1.push("youtube.com")
x1.push("youtube.music.com")
x1.size()
x1.traverseAndPrint()

print("Linked list setelah di pop:")   
x1.pop()
x1.traverseAndPrint()
x1.peek()
x1.size()