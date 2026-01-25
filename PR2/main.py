import math

print("Решение кравнения")
x = int(input("Введите x "))
y = int(input("Введите y "))
z = int(input("Введите z "))
s = (5 * math.atan(x)) - ((1/4) * math.acos(x)) * ( ((x+3) * math.fabs(x-y)) + math.pow(x,2))/( math.fabs(x-y) * z + math.pow(x,2) )
print(s)