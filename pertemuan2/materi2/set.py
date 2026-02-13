#PYTHON SET
#Set
thisset = {"apple", "banana", "cherry"}
print(thisset) #Set tidak berurutan, jadi tidak dapat dipastikan urutan item yang akan muncul

#Unordered
#-> Item dalam set dapat muncul dalam urutan yang berbeda setiap kali digunakan, dan tidak dapat dirujuk berdasarkan indeks atau kunci.

#Unchanged
#-> Setelah sebuah set dibuat, item di dalamnya tidak dapat diubah, tetapi masih dapat menghapus dan menambahkan item baru.

#Duplicate Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Set Length
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

"""
set1 = ["abc", 34, True, 40, "male"] 
# set1 memiliki tipe data string, int, dan boolean
"""

#set()
myset = {"apple", "banana", "cherry"}
print(type(myset))


#ACCESS SET ITEMS
#Access Item
#-> Use For Loop
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#-> Use in Keyword
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Setelah sebuah set dibuat, item di dalamnya tidak dapat diubah, tetapi item baru dapat ditambahkan.


#ADD SET ITEMS
#Add Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Add Items from Another Set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Add any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


#REMOVE SET ITEM
#Remove Item
#-> remove() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") # jika ("") akan error
print(thisset)

#-> discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") # jika ("") tidak akan error
print(thisset)

#-> pop() method --> menghapus suatu item secara acak
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #set after removal

#-> clear() method --> mengosongkan set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#-> del keyword --> menghapus keseluruhan set
thisset = {"apple", "banana", "cherry"}
del thisset


#LOOP SET
#Loop Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


#JOIN SET
#union() method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) #bisa juga menggunakan operator |, contoh set3 = set1 | set2
print(set3)

#-> dengan operator |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

#-> join Multiple Set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4) #bisa juga menggunakan operator |, contoh myset = set1 | set2 | set3 | set4
print(myset)

#-> update() method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#intersection() method --> mengembalikan set baru
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2) #bisa juga menggunakan operator &, contoh: set3 = set1 & set2. Tapi ingat, hanya bisa digunakan antar set saja.
print(set3)

#-> intersection_update() method --> mengubah set asli
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

#difference() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) #sama seperti method lain, method ini bisa menggunakan operator - . Aturannya juga sama seperti method lain.
print(set3)

#-> difference_update() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

#-> symmetric_difference() method --> menyimpan elemen yang tidak ada di kedua set tanpa mengubah set asli
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

#--> symmetric_difference_update() method --> menyimpan elemen yang tidak ada di kedua set dengan mengubah set asli
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)


#PYTHON FROZENSET
#Frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
