#Boolean Value
print(3.9 > -9)
print(3.9 < -9)

a = 3.9
b = -9

if b == a :
  print("b sama dengan a")
else:
  print("b tidak sama dengan a")

#Evaluate Value and variable
x = "Edo"
y = 15
z = 0
X = -1

print(bool(x))
print(bool(y))
print(bool(z))
print(bool(X))

#Kebanyakan value bernilai true, berikut beberapa value yang bernilai false:
"""
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
"""

#Function can Return a Boolean
#Print "Ya" jika return true, jika false maka "Tidak"
def myFunction() :
  return 0

if myFunction():
  print("Ya")
else:
  print("Tidak")

#isinstance function
x = 29.9
print(isinstance(x,float))