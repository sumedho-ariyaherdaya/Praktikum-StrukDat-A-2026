nilai = [75, 80, 65, 90, 85]
nilai.append(95)
nilai.remove(65)
nilai.sort()
min = nilai[0]
max = nilai[-1]
jumlah_data = (len(nilai))
jumlah_nilai = 0
for i in (nilai):
    jumlah_nilai+=i
rata_rata = jumlah_nilai/jumlah_data
print(nilai)
print("max:", max, "min:",min, "jumlah data:", jumlah_data)
print("rata rata:", rata_rata)
