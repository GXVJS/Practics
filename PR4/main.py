n = int(input("Введите число n: "))

factorial = 1
sum_of_factorials = 0

for i in range(1, n + 1):
    factorial *= i  # вычисляем i-й факториал
    sum_of_factorials += factorial  # добавляем к сумме

print("Сумма факториалов от 1! до", n, ": ", sum_of_factorials)