#PYTHON ENCAPSULATION
#Private Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
#print(p1.__age) # Ketika di run, akan menghasilkan error

#Getter
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Provate properties

  def get_age(self): # Metode getter
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age()) # Memanggil metode getter untuk mengakses private properties

#Setter
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private properties

  def get_age(self): # Metode Getter
    return self.__age

  def set_age(self, age): # Metode Setter
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())

p1.set_age(26) # Memodifikasi nilai pada properti age
print(p1.get_age()) # Mencetak nilai pada private properti age yang telah dimodifikasi

#Protected Properties
class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Bisa diakses tapi tidak disarankan

#Private Method -> digunakan hanya ketika method tsb digunakan di class itu saja
class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num): # Private Method
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # Akan menghasilkan error

#Name Mangling
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Tidak disarankan