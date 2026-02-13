#PYTHON TUPLE
#Ordered
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Unchangeable
#-> tuple bersifat tidak dapat diubah, seperti menambah atau menghapus item pada tuple setelah tuple dibuat.

#Allow Duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

"""
tuple1 = ("abc", 34, True, 40, "male") 
# tuple1 memiliki tipe data string, int, dan boolean
"""

#Create Tuple with One Item
thistuple = ("apple",) #Wajib ada tanda koma setelah item, jika tidak, Pyhton tidak akan mengenalinya sebagai tuple.
print(type(thistuple))

#Not a tuple
thistuple = ("apple")
print(type(thistuple))

#type()
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


#ACCESS TUPLE ITEMS
#Access Item
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) 

#Range of Negative Indexing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple [-4:-1])

#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits list")


#UPDATE TUPLES
#Change Tuple Value
x = ("apple", "banana", "cherry")
y = list(x) # Ubah tuple menjadi list
y[1] = "kiwi" # Ubah item indeks ke [1] (banana) menjadi kiwi pada tuple yang sudah menjadi list 
x = tuple(y) # Ubah list menjadi tuple kembali

print(x)

#Add Item
#-> Convert to list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple) # Ubah menjadi list
y.append("orange") # Tambahkan orange
thistuple = tuple(y) # Ubah kembali menjadi tuple

print(thistuple)

#-> Add tuple to tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

"""
#remove all with del function
thistuple = ("apple", "banana", "cherry")
del thistuple

print(thistuple) #this will raise an error because the tuple no longer exists
"""


#LOOP TUPLES
#Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Loop Through the Index Number
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


#JOIN TUPLES
#Using + Operator
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply Tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)