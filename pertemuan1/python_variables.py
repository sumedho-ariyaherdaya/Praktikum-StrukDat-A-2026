#PYTHON VARIABLE
#Creating Variables
a = 10
b = "Sumedho"
print (a)
print (b)

x = 3      # tipe data x 3
x = "Edo" # tipe data x menjadi str
print(x)

#Casting
X = complex(4)    # X akan menjadi (4 + 0j)
Y = bytes(4)    # Y akan menjadi byte
Z = float(4)  # Z akan menjadi 4.0
print(X)
print(Y)
print(Z)

#Case Sensistive (variabel x dan X dibedakan dalam python)

#Get the Type
print(type(x))
print(type(X))
print(type(Y))
print(type(Z))

#Single or Double quotes
A = "Sumedho"
B = 'Sumedho'
print(A)
print(B)


#VARIABLE NAMES
variabelsaya = "sumedhoariya"
variabelsaya = "sumedho_ariya"
_variabel_saya = "_sumedho_ariya"
variabelSaya = "sumedhoAriya"
VARIABELSAYA = "SUMEDHOARIYA"
variabelsaya1 = "sumedhoariya1"
print(variabelsaya)
print(variabelsaya)
print(_variabel_saya)
print(variabelSaya)
print(VARIABELSAYA)
print(variabelsaya1)

namaVariabelSaya = "camelCase"
NamaVariabelSaya = "PascalCase"
nama_variabel_saya = "snake_case"
print(namaVariabelSaya)
print(NamaVariabelSaya)
print(nama_variabel_saya)


#ASSIGN MULTIPLE VALUES
#Many value to multiple variable
x, y, z = "Alpro", "StrukDat", "Arsikom"
print(x)
print(y)
print(z)

#One value to multiple variable
a = b = c = d = "StrukDat"
print(a)
print(b)
print(c)
print(d)

#Unpack a Collection in a list, tuple, etc
matkul = ["Alpro", "StrukDat", "Arsikom"]
X, Y, Z = matkul
print(X)
print(Y)
print(Z)


#OUTPUT VARIABLE
x = "Python"
y = "keren"
print(x, y)

#Bisa juga gunakan operator +, tapi tidak bisa kombinasi antara string dan nomor
a = "Python"
b = "keren"
c = "dan"
d = "seru"
print(a + b + c + d) 

#khusus untuk yang pake operator +, jangan lupa whitespace setelah setiap kata
a = "Python "
b = "keren "
c = "dan "
d = "seru"
print(a + b + c + d) 

#untuk variable yang berisi angka juga bisa pakai operator aritmatika
x = 10
y = 3
print(x - y)


#GLOBAL VARIABLES (bisa menggunakan variabel diluar fungsi)
e = "keren" # -> global variable
f = "luarbiasa"

def myfunc():
    print("Python " + e + ", " + f)

myfunc()

#Jika ada variabel dengan nama yang sama di dalam sebuah fungsi, variabel ini akan bersifat lokal dan hanya dapat digunakan di dalam fungsi tersebut
e = "keren"
f = "luarbiasa"

def myfunc():
    e = "mantap" #-> local variable
    print("Python " + e + ", " + f)

myfunc()

print("Python " + e + ", " + f)

#Umumnya, variabel pada fungsi adalah variabel lokal, untuk membuatnya menjadi variabel globab gunakan kata kunci global.
def myfunc():
    global e
    e = "mantap" #-> local variable yang sudah menjadi global variable

myfunc()
print("Python " + e) 