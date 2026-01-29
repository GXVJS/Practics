import math

print("=" * 50)
print("Практическая номер 7")
print("=" * 50)

# Вариант 1.1: Площади геометрических фигур
print("\nВар.1.1: Вычисление площадей геометрических фигур")

def calculate_area():
    print("\nВыберите фигуру:")
    print("1. Квадрат")
    print("2. Прямоугольник")
    print("3. Треугольник")
    print("4. Круг")
    print("5. Трапеция")

    choice = input("\nВведите номер фигуры (1-5): ")

    if choice == '1':  # Квадрат
        side = float(input("Введите длину стороны квадрата: "))
        area = side ** 2
        print(f"Площадь квадрата со стороной {side} = {area:.2f}")

    elif choice == '2':  # Прямоугольник
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        area = length * width
        print(f"Площадь прямоугольника {length}x{width} = {area:.2f}")

    elif choice == '3':  # Треугольник
        print("Выберите способ вычисления:")
        print("1. По основанию и высоте")
        print("2. По трем сторонам (формула Герона)")
        triangle_choice = input("Введите 1 или 2: ")

        if triangle_choice == '1':
            base = float(input("Введите основание треугольника: "))
            height = float(input("Введите высоту треугольника: "))
            area = 0.5 * base * height
            print(f"Площадь треугольника = {area:.2f}")
        elif triangle_choice == '2':
            a = float(input("Введите первую сторону: "))
            b = float(input("Введите вторую сторону: "))
            c = float(input("Введите третью сторону: "))
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c) / 2
                area = math.sqrt(p * (p - a) * (p - b) * (p - c))
                print(f"Площадь треугольника = {area:.2f}")
            else:
                print("Такой треугольник не существует")

    elif choice == '4':  # Круг
        radius = float(input("Введите радиус круга: "))
        area = math.pi * radius ** 2
        print(f"Площадь круга с радиусом {radius} = {area:.2f}")

    elif choice == '5':  # Трапеция
        a = float(input("Введите верхнее основание трапеции: "))
        b = float(input("Введите нижнее основание трапеции: "))
        h = float(input("Введите высоту трапеции: "))
        area = 0.5 * (a + b) * h
        print(f"Площадь трапеции = {area:.2f}")

    else:
        print("Неверный выбор!")

# Запуск программы для варианта 1.1
calculate_area()

# Вариант 2.1: Площадь правильного шестиугольника
print("\n\nВар.2.1: Площадь правильного шестиугольника")

def triangle_area(side):
    """Площадь равностороннего треугольника"""
    return (math.sqrt(3) / 4) * side ** 2

def hexagon_area(side):
    """Площадь правильного шестиугольника (6 равносторонних треугольников)"""
    return 6 * triangle_area(side)

a = float(input("Введите сторону правильного шестиугольника: "))
area_hex = hexagon_area(a)
print(f"Площадь правильного шестиугольника со стороной {a} = {area_hex:.2f}")
print(f"(Площадь одного треугольника: {triangle_area(a):.2f})")

# Вариант 3.1: Гипотенузы двух прямоугольных треугольников
print("\n\nВар.3.1: Сравнение гипотенуз двух треугольников")

def hypotenuse(a, b):
    """Вычисление длины гипотенузы"""
    return math.sqrt(a ** 2 + b ** 2)

print("Введите катеты первого треугольника:")
a1 = float(input("Первый катет: "))
b1 = float(input("Второй катет: "))

print("Введите катеты второго треугольника:")
a2 = float(input("Первый катет: "))
b2 = float(input("Второй катет: "))

hyp1 = hypotenuse(a1, b1)
hyp2 = hypotenuse(a2, b2)

print(f"\nГипотенуза первого треугольника: {hyp1:.2f}")
print(f"Гипотенуза второго треугольника: {hyp2:.2f}")

if hyp1 > hyp2:
    print(f"Гипотенуза первого треугольника больше")
elif hyp2 > hyp1:
    print(f"Гипотенуза второго треугольника больше")
else:
    print("Гипотенузы равны")

# Вариант 4.1: Деление дробей с приведением к несократимой дроби
print("\n\nВар.4.1: Деление дробей A/B ÷ C/D")


def gcd(a, b):
    """Алгоритм Евклида для нахождения НОД"""
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    """Сокращение дроби"""
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor

A = int(input("Введите числитель первой дроби A: "))
B = int(input("Введите знаменатель первой дроби B: "))
C = int(input("Введите числитель второй дроби C: "))
D = int(input("Введите знаменатель второй дроби D: "))

# Деление дробей: (A/B) ÷ (C/D) = (A/B) * (D/C) = (A*D)/(B*C)
result_numer = A * D
result_denom = B * C

# Сокращаем дробь
simplified_numer, simplified_denom = simplify_fraction(result_numer, result_denom)

print(f"\n({A}/{B}) ÷ ({C}/{D}) = ({result_numer}/{result_denom})")
print(f"После сокращения: {simplified_numer}/{simplified_denom}")

# Вариант 5.1: Вычитание дробей с приведением к несократимой дроби
print("\n\nВар.5.1: Вычитание дробей A/B - C/D")

A = int(input("Введите числитель первой дроби A: "))
B = int(input("Введите знаменатель первой дроби B: "))
C = int(input("Введите числитель второй дроби C: "))
D = int(input("Введите знаменатель второй дроби D: "))

# Вычитание дробей: (A/B) - (C/D) = (A*D - C*B)/(B*D)
result_numer = A * D - C * B
result_denom = B * D

# Сокращаем дробь
simplified_numer, simplified_denom = simplify_fraction(abs(result_numer), result_denom)

# Учитываем знак
if result_numer < 0:
    sign = "-"
    simplified_numer = abs(simplified_numer)
else:
    sign = ""

print(f"\n({A}/{B}) - ({C}/{D}) = ({result_numer}/{result_denom})")
print(f"После сокращения: {sign}{simplified_numer}/{simplified_denom}")

# Вариант 6.1: НОД и НОК двух чисел
print("\n\nВар.6.1: НОД и НОК двух натуральных чисел")

def gcd_euclid(a, b):
    """НОД по алгоритму Евклида"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """НОК через НОД"""
    return abs(a * b) // gcd_euclid(a, b)

num1 = int(input("Введите первое натуральное число: "))
num2 = int(input("Введите второе натуральное число: "))

nod = gcd_euclid(num1, num2)
nok = lcm(num1, num2)

print(f"\nНОД({num1}, {num2}) = {nod}")
print(f"НОК({num1}, {num2}) = {nok}")
print(f"Проверка: ({num1} * {num2}) / {nod} = {nok}")

# Вариант 7.1: Площадь четырехугольника с прямым углом
print("\nВар.7.1: Площадь четырехугольника с прямым углом")

def right_triangle_area(a, b):
    return 0.5 * a * b

def triangle_area_heron(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def quadrilateral_area(X, Y, Z, T):
    # Диагональ (гипотенуза) между сторонами X и Y
    diagonal = math.sqrt(X ** 2 + Y ** 2)

    # Площадь четырехугольника = площадь прямоугольного треугольника (X,Y) + площадь треугольника (Z,T,диагональ)
    area1 = right_triangle_area(X, Y)

    # Проверяем существование второго треугольника
    if diagonal + Z > T and diagonal + T > Z and Z + T > diagonal:
        area2 = triangle_area_heron(diagonal, Z, T)
        return area1 + area2
    else:
        return None  # Такой четырехугольник не существует

print("Введите длины сторон четырехугольника X, Y, Z, T:")
X = float(input("X: "))
Y = float(input("Y: "))
Z = float(input("Z: "))
T = float(input("T: "))

area = quadrilateral_area(X, Y, Z, T)
if area is not None:
    print(f"Площадь четырехугольника = {area:.2f}")
    print(f"(Диагональ = {math.sqrt(X ** 2 + Y ** 2):.2f})")
else:
    print("Такой четырехугольник не существует")

# Вариант 8.1: Числа, делящиеся на каждую из своих цифр
print("\n\nВар.8.1: Числа, делящиеся на каждую из своих цифр")

def divides_by_all_digits(n):
    """Проверяет, делится ли число на каждую из своих цифр"""
    original_n = n
    while n > 0:
        digit = n % 10
        if digit == 0 or original_n % digit != 0:
            return False
        n //= 10
    return True

n = int(input("Введите натуральное число n: "))
print(f"Числа, не превосходящие {n}, которые делятся на каждую из своих цифр:")

found = False
for i in range(1, n + 1):
    if divides_by_all_digits(i):
        print(i, end=" ")
        found = True

if not found:
    print("Таких чисел нет")

# Вариант 9.1: Сколько раз вычесть сумму цифр до нуля
print("\n\nВар.9.1: Сколько раз вычесть сумму цифр до нуля")

def sum_of_digits(n):
    """Сумма цифр числа"""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = int(input("Введите натуральное число: "))
original_num = num
steps = 0

print(f"Процесс:")
while num > 0:
    digit_sum = sum_of_digits(num)
    print(f"{num} - {digit_sum} = {num - digit_sum}")
    num -= digit_sum
    steps += 1

print(f"Число {original_num} достигнет нуля за {steps} шагов")

# Вариант 10.1: Числа из цифр a, b, c на отрезке [100, N]
print("\n\nВар.10.1: Числа из цифр a, b, c на отрезке [100, N]")


def is_composed_of_digits(num, a, b, c):
    """Проверяет, состоит ли число только из цифр a, b, c"""
    digits = {a, b, c}
    original_num = num

    if num == 0 and 0 in digits:
        return True

    while num > 0:
        digit = num % 10
        if digit not in digits:
            return False
        num //= 10
    return True

N = int(input("Введите N (210 < N < 231): "))
if not (210 < N < 231):
    N = 220  # Значение по умолчанию
    print(f"Некорректное N. Установлено значение {N}")

print("Введите три цифры a, b, c:")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(f"\nЧисла на отрезке [100, {N}], состоящие только из цифр {a}, {b}, {c}:")
count = 0
for i in range(100, N + 1):
    if is_composed_of_digits(i, a, b, c):
        print(i, end=" ")
        count += 1

print(f"\nВсего таких чисел: {count}")

# Вариант 11.1: Пары "близнецов" на отрезке [n, 2n]
print("\n\nВар.11.1: Пары простых чисел-близнецов на отрезке [n, 2n]")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Введите натуральное число n > 2: "))
if n <= 2:
    n = 3
    print(f"n должно быть > 2. Установлено n = {n}")

print(f"Пары простых чисел-близнецов на отрезке [{n}, {2 * n}]:")
found_twins = False
for i in range(n, 2 * n - 1):
    if is_prime(i) and is_prime(i + 2):
        print(f"({i}, {i + 2})")
        found_twins = True

if not found_twins:
    print("Простых чисел-близнецов на этом отрезке нет")

# Вариант 12.1: Пары дружественных чисел
print("\nВар.12.1: Пары дружественных чисел до N")

def sum_of_proper_divisors(n):
    """Сумма собственных делителей числа (кроме самого числа)"""
    if n <= 1:
        return 0
    total = 1  # 1 всегда делитель
    limit = int(math.sqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # добавляем парный делитель
                total += n // i
    return total

N = int(input("Введите натуральное число N: "))
print(f"Пары дружественных чисел, не превышающих {N}:")

friends = set()
for a in range(1, N + 1):
    b = sum_of_proper_divisors(a)
    if b > a and b <= N:  # b > a чтобы избежать дублирования
        if sum_of_proper_divisors(b) == a:
            friends.add((a, b))
            print(f"({a}, {b})")

if not friends:
    print("Дружественных чисел не найдено")

# Вариант 13.1: Числа Армстронга
print("\n\nВар.13.1: Числа Армстронга от 1 до k")

def is_armstrong(num):
    """Проверка, является ли число числом Армстронга"""
    digits = [int(d) for d in str(num)]
    n = len(digits)
    return sum(d ** n for d in digits) == num

k = int(input("Введите число k: "))
print(f"Числа Армстронга от 1 до {k}:")

armstrong_numbers = []
for i in range(1, k + 1):
    if is_armstrong(i):
        armstrong_numbers.append(i)
        print(i, end=" ")

if not armstrong_numbers:
    print("Чисел Армстронга не найдено")
print(f"\nВсего найдено: {len(armstrong_numbers)}")

# Вариант 14.1: Числа с наибольшим количеством делителей
print("\n\nВар.14.1: Числа с наибольшим количеством делителей")

def count_divisors(n):
    """Количество делителей числа"""
    if n == 0:
        return 0
    count = 2  # 1 и само число
    limit = int(math.sqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count

M = int(input("Введите M: "))
N = int(input("Введите N (M <= N): "))

if M > N:
    M, N = N, M

max_divisors = 0
numbers_with_max_divisors = []

for i in range(M, N + 1):
    div_count = count_divisors(i)
    if div_count > max_divisors:
        max_divisors = div_count
        numbers_with_max_divisors = [i]
    elif div_count == max_divisors:
        numbers_with_max_divisors.append(i)

print(f"\nЧисла из интервала [{M}, {N}] с наибольшим количеством делителей ({max_divisors}):")
for num in numbers_with_max_divisors:
    print(num, end=" ")
print(f"\nВсего таких чисел: {len(numbers_with_max_divisors)}")

# Вариант 15.1: Простые числа с палиндромной двоичной записью
print("\n\nВар.15.1: Простые числа с палиндромной двоичной записью")

def is_prime(num):
    """Проверка числа на простоту"""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_binary_palindrome(num):
    """Проверка, является ли двоичная запись числа палиндромом"""
    binary = bin(num)[2:]  # Преобразуем в двоичную строку
    return binary == binary[::-1]

n = int(input("Введите натуральное число n: "))
print(f"Простые числа до {n} с палиндромной двоичной записью:")

prime_palindromes = []
for i in range(2, n + 1):
    if is_prime(i) and is_binary_palindrome(i):
        prime_palindromes.append(i)
        binary_str = bin(i)[2:]
        print(f"{i} (в двоичной: {binary_str})")

if not prime_palindromes:
    print("Таких чисел не найдено")
print(f"Всего найдено: {len(prime_palindromes)}")

