class Person:
    def __init__(self, nama, tinggi, umur):
        self.nama = nama
        self.tinggi = tinggi
        self.umur = umur

class Karyawan(Person):
    def __init__(self, nama, tinggi, umur, gaji):
        super().__init__(nama, tinggi, umur)
        self._gaji = gaji
    
    def get_gaji(self):
        return self._gaji

class Rekening:
    def __init__(self, noRek):
        self.noRek = noRek
        self.__pin = ""

    def set_pin(self, pin):
        if pin > 8:
            self._pin = pin
        else:
            print("Pin harus terdiri dari 8 karakter")
    
    def get_pin(self):
        return self.__pin
    

p1 = Person("Edo", 167, 18)
print(p1.nama)

p2 = Karyawan("Edo", 167, 18, 4000000)
print(p2.get_gaji())

p3 = Rekening(11223344)
p3.set_pin(12345678)
p3.get_pin()