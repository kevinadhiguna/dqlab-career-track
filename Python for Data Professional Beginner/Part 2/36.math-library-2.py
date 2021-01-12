# Import library math
import math
# Fungsi math.log()
print(">>> Fungsi math.log()")
# x = log basis 2 dari 8
x = math.log(8,2)
# y = log basis 3 dari 81
y = math.log(81,3)
# z = log basis 10 dari 10000
z = math.log(10000,10)
print(x)
print(y)
print(z)
# Fungsi math.sqrt()
print(">>> Fungsi math.sqrt()")
# akar kuadrat dari 100
x = math.sqrt(100)
print(x)
# akar kuadrat dari 2
y = math.sqrt(2)
print(y)
# Fungsi math.copysign()
print(">>> Fungsi math.copysign()")
x = 10.32
y = -13.87
z = -15
x = math.copysign(x,z)
y = math.copysign(y,z)
z = math.copysign(z,10)
print(x)
print(y)
print(z)