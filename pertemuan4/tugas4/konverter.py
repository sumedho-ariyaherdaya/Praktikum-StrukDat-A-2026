import kurs
import format_uang
def konversi_mata_uang():
    impor_kurs = kurs.kurs_data
    impor_nama_uang = kurs.nama_mata_uang 

    # Menampilkan error jika inputan tidak sesuai pilihan
    while True:
        try:
            dari_mata_uang = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
            if dari_mata_uang not in impor_kurs and dari_mata_uang != "IDR":
                raise KeyError
            ke_mata_uang = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper() 
            if ke_mata_uang not in impor_kurs and ke_mata_uang != "IDR":
                raise KeyError
            break
        except KeyError:
            print("Error: Mata uang belum terdaftar! Perhatikan inputan anda (tidak boleh ada spasi)")
       
    # Menampilkan error jika inputan bukan angka
    while True:
        try:
            jumlah_mata_uang = float(input("Jumlah: "))
        except ValueError:
            print("Error: Nilai mata uang tidak valid! Harap masukkan bilangan bulat")
        else:
            break

    # Konversi uang 
    match dari_mata_uang:
            case "IDR" | "USD" | "EUR" | "SGD" | "JPY":
                # Jika mata uang asal == mata uang tujuan
                if dari_mata_uang == ke_mata_uang:
                    if dari_mata_uang == "IDR" and ke_mata_uang == "IDR":
                        print(f"{impor_nama_uang[dari_mata_uang]} {format_uang.format_nilai_uang(jumlah_mata_uang)} = {impor_nama_uang[ke_mata_uang]} {format_uang.format_nilai_uang(jumlah_mata_uang)}")
                    else:
                        print(f"{format_uang.format_nilai_uang(jumlah_mata_uang)} {impor_nama_uang[dari_mata_uang]} = {format_uang.format_nilai_uang(jumlah_mata_uang)} {impor_nama_uang[ke_mata_uang]}")
                    
                # IDR ke USD/EUR/SGD/JPY
                elif dari_mata_uang == "IDR" and ke_mata_uang in impor_kurs:
                    hasil_konversi = jumlah_mata_uang/impor_kurs[ke_mata_uang]
                    print(f"{impor_nama_uang[dari_mata_uang]}{format_uang.format_nilai_uang(jumlah_mata_uang)} = {format_uang.format_nilai_uang(hasil_konversi)} {impor_nama_uang[ke_mata_uang]}")
                
                # USD/EUR/SGD/JPY ke IDR
                elif dari_mata_uang in impor_kurs and ke_mata_uang == "IDR":
                    hasil_konversi = jumlah_mata_uang*impor_kurs[dari_mata_uang]
                    print(f"{format_uang.format_nilai_uang(jumlah_mata_uang)} {impor_nama_uang[dari_mata_uang]} = {impor_nama_uang[ke_mata_uang]}{format_uang.format_nilai_uang(hasil_konversi)}")
                
                # Mata uang asing ke mata uang asing lainnya
                elif dari_mata_uang in impor_kurs and ke_mata_uang in impor_kurs:
                    hasil_konversi = (jumlah_mata_uang*impor_kurs[dari_mata_uang])/impor_kurs[ke_mata_uang]
                    print(f"{format_uang.format_nilai_uang(jumlah_mata_uang)} {impor_nama_uang[dari_mata_uang]} = {format_uang.format_nilai_uang(hasil_konversi)} {impor_nama_uang[ke_mata_uang]}")

