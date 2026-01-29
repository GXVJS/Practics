import math

print("=" * 50)
print("18 ПРОСТЫХ ЗАДАЧ НА PYTHON")
print("=" * 50)

# 1. Сравнение двух чисел и вывод наибольшего
print("\n1. Сравнение двух чисел:")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if num1 > num2:
    print(f"Наибольшее число: {num1}")
elif num2 > num1:
    print(f"Наибольшее число: {num2}")
else:
    print("Числа равны")

# 2. Проверка числа на четность
print("\n2. Проверка на четность:")
num = int(input("Введите целое число: "))
if num % 2 == 0:
    print(f"Число {num} четное")
else:
    print(f"Число {num} нечетное")

# 3. Разделение числа на четные и нечетные цифры
print("\n3. Разделение цифр на четные и нечетные:")
num = input("Введите число: ")
even_digits = []
odd_digits = []
for digit in num:
    if digit.isdigit():
        if int(digit) % 2 == 0:
            even_digits.append(digit)
        else:
            odd_digits.append(digit)
print(f"Четные цифры: {even_digits}")
print(f"Нечетные цифры: {odd_digits}")

# 4. Проверка числа на простоту
print("\n4. Проверка на простое число:")
num = int(input("Введите натуральное число: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"Число {num} простое")
else:
    print(f"Число {num} составное")

# 5. Вычисление среднего арифметического трех чисел
print("\n5. Среднее арифметическое трех чисел:")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))
average = (num1 + num2 + num3) / 3
print(f"Среднее арифметическое: {average:.2f}")

# 6. Проверка числа на кратность 7
print("\n6. Проверка на кратность 7:")
num = float(input("Введите число: "))
if num % 7 == 0:
    print(f"Число {num} кратно 7")
else:
    print(f"Число {num} не кратно 7")

# 7. Определение, является ли год високосным
print("\n7. Проверка года на високосность:")
year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Год {year} високосный")
else:
    print(f"Год {year} не високосный")

# 8. Подсчет количества дней в месяце
print("\n8. Количество дней в месяце:")
month = int(input("Введите номер месяца (1-12): "))
if month == 2:
    year = int(input("Введите год для проверки февраля: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days = 29
    else:
        days = 28
elif month in [4, 6, 9, 11]:
    days = 30
elif month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
else:
    days = "некорректный номер месяца"
print(f"В месяце {month}: {days} дней")

# 9. Расчет площади треугольника по формуле Герона
print("\n9. Площадь треугольника по формуле Герона:")
a = float(input("Введите первую сторону: "))
b = float(input("Введите вторую сторону: "))
c = float(input("Введите третью сторону: "))
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Площадь треугольника: {area:.2f}")
else:
    print("Такой треугольник не существует")

# 10. Проверка на равенство трех чисел
print("\n10. Проверка равенства трех чисел:")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))
if num1 == num2 == num3:
    print("Все три числа равны")
else:
    print("Числа не равны между собой")

# 11. Проверка возраста пользователя
print("\n11. Проверка возраста:")
age = int(input("Введите ваш возраст: "))
if age < 0:
    print("Возраст не может быть отрицательным")
elif age < 18:
    print("Вы несовершеннолетний")
elif 18 <= age < 60:
    print("Вы взрослый")
else:
    print("Вы пожилой человек")

# 12. Проверка числа на положительное/отрицательное
print("\n12. Проверка знака числа:")
num = float(input("Введите число: "))
if num > 0:
    print("Число положительное")
elif num < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

# 13. Количество дней в феврале
print("\n13. Количество дней в феврале:")
year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"В феврале {year} года 29 дней (високосный год)")
else:
    print(f"В феврале {year} года 28 дней")

# 14. Принадлежность точки квадрату
print("\n14. Принадлежность точки квадрату (0,0)-(5,5):")
x = float(input("Введите координату X: "))
y = float(input("Введите координату Y: "))
if 0 <= x <= 5 and 0 <= y <= 5:
    print(f"Точка ({x}, {y}) принадлежит квадрату")
else:
    print(f"Точка ({x}, {y}) не принадлежит квадрату")

# 15. Сумма и разность двух чисел
print("\n15. Сумма и разность двух чисел:")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
sum_result = num1 + num2
diff_result = num1 - num2
print(f"Сумма: {sum_result}")
print(f"Разность: {diff_result}")

# 16. Кратность 3 и 5
print("\n16. Проверка на кратность 3 и 5:")
num = int(input("Введите целое число: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"Число {num} кратно и 3, и 5")
elif num % 3 == 0:
    print(f"Число {num} кратно только 3")
elif num % 5 == 0:
    print(f"Число {num} кратно только 5")
else:
    print(f"Число {num} не кратно ни 3, ни 5")

# 17. Проверка на вековой год
print("\n17. Проверка на вековой год:")
year = int(input("Введите год: "))
if year % 100 == 0:
    print(f"Год {year} вековой")
else:
    print(f"Год {year} не вековой")

# 18. Проверка числа на целое/дробное
print("\n18. Проверка числа на целое/дробное:")
num_str = input("Введите число: ")
try:
    num = float(num_str)
    if num.is_integer():
        print(f"Число {int(num)} целое")
    else:
        print(f"Число {num} дробное")
except ValueError:
    print("Это не число!")

print("\n" + "=" * 50)
print("Все задачи выполнены!")
print("=" * 50)