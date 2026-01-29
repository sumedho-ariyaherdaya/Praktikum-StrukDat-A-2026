print("Sumedho") # double quotes
print('Sumedho') # single quotes

#Quotes Inside Quotes
print("Namaku Sumedho, biasanya dipanggil 'edo', aku dari 'Dumai'")
print('Namaku Sumedho, biasanya dipanggil "edo", aku dari "Dumai"')

#Multiline string
x = """ Namaku Sumedho Ariya Herdaya, Aku adalah angkatan '25' di prodi TI Universitas Riau """
print(x)
X = ''' Namaku Sumedho Ariya Herdaya, Aku adalah angkatan "25" di prodi TI Universitas Riau  '''
print(X)

#String are Arrays (urutan huruf pada string mirip dengan konsep array)
a = "Hello, World!"
print(a[-1]) #ini akan mengeluarkan output berupa !

#Looping Through a String (menulis kembali semua huruf satu persatu secara berulang hingga semua huruf ditampilkan)
for b in "apel, nanas dan tomat":
  print(b) 

#String Length (menghtiung panjang string)
B = "apel, nanas dan tomat"
print(len(B)) 

#Check String
c = "apel, nanas dan tomat"
if " "in c:
  print("iya, '' ada di dalam string")


#SLICING STRING
#Slice From the Start (awal ke target)
d = "Aduh h, World!"
print(d[:7])

#Slice to the End (dari batas yg ditentukan hingga akhir)
d = "Aduh h,  World!"
print(d[3:])

d = "Aduh h,  World!"
print(d[3:7])

#Negative Indexing (0 dimulai dari huruf pertama, - dimulai dari huruf paling kanan)
d = "Aduh h,  World!"
print(d[-6: -3])


#MODIFY STRING
#Upper Case 
e = "Sumedho Ariya Herdaya"
print(e.upper())

#Lower Case
e = "Sumedho Ariya Herdaya"
print(e.lower())

#Remove Whitespace
e =" Sumedho Ariya Herdaya"
print(e.strip())

#Replace String
e = "sumedho ariya herdaya"
print(e.replace("h", "j"))

e = "Sumedho Ariya Herdaya"
print(e.replace("h", "j")) #yang ke replace 'h', 'H' tidak ke replace

#Split String
e = "Sumedho. .Ariya . Herdaya."
print(e.split(".")) #['Sumedho', ' ', 'Ariya ', ' Herdaya', ''] 


#STRING CONCATENATION (kuranglebih penggabungan 2 string menggunakan operator +)
f = "Sumedho"
g = "Ariya"
h = "Herdaya"
i = f + g + h
print(i)
#untuk menambahkan spasi gunakan " "
f = "Sumedho"
g = "Ariya"
h = "Herdaya"
i = f + " " + g + " " + h
print(i)


#FORMAT STRING (untuk mengkombinasikan string dan nomor, gunakan f-string
#F-string
akt = 25
teks = f"Nama saya Edo, saya angkatan {akt}"
print(teks)

#Placeholder and modifier
akt = 5
teks = f"Nama saya Edo, saya angkatan {akt * 5}"
print(teks)

#Escape Character 
j = 'Hari ini hari Jum\'at' #jika tidak ada \' pada kata Jum'at, maka akan error
print(j)
j = 'Hari ini hari Jum\'at \\ hari Sabtu?' #yang ditampilkan hanya "\""
print(j)
j = 'Hari ini \nhari Jum\'at' #kata setelah "\n" menjadi baris baru
print(j)
j = 'Hari ini \rhari Jum\'at' #kata setelah "\r" menjadi hilang
print(j)
j = 'Hari ini \thari Jum\'at' #memberikan whitespace sebesar tab setelah "\t"
print(j)
j = 'Hari ini \bhari Jum\'at' #backspace
print(j)
j = 'Hari ini \fhari Jum\'at' #menghapus semua kata sebelum "\f"
print(j)
j = "\111\222\333" #Octal value, jika terdapat sebuah \ yang diikuti 3 bilangan integer akan menghasilkan sebuah nilai octal
print(j) 
j = "\x22\x33\x44\x31" #sama seperti octal, bedanya hex pakai x dan akan menghasilkan nomor hex
print(j) 


#STRING METHOD
k = "Sumedho Ariya Herdaya"
l = k.capitalize() #Menjadikan karakter pertama Kapital
print(l)

k = "Sumedho Ariya Herdaya"
l = k.casefold() #Menjadikan string non kaptal
print(l)

k = "Sumedho"
l = k.center(10) #Membuat teks ke tengah sesuai space yg ditentukan
print(l)

k = "Sumedho Ariya Herdaya" 
l = k.find("Ariya")#mencari sebuah string
print(l)

k = "sumedho ariya herdaya"
l = k.title() #Membuat huruf pertama setiap kata menjadi kapital
print(l) #dan masih banyak lagi