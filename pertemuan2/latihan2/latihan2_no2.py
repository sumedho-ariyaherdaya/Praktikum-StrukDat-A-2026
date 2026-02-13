dosen = ("D001", "Dr.Andi", "Struktur Data", 12)
print(dosen[1:3])
for x in dosen:
    print(dosen)
y = list(dosen) #arraynya harus diubah ke list dulu, karena tuple tidak bisa diubah 
y[-1] = 14
dosen = tuple(y)
print(dosen) #nilai pada tuple indeks ke -1 berubah menjadi 14
#salah satu kelebihan ppada tuple adalah nilainya tidak dapat diubah atau tetap.