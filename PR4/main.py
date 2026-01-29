print("=" * 50)
print("10 ЗАДАЧ НА ЦИКЛЫ В PYTHON")
print("=" * 50)

# 1. Вывести все числа от A до B включительно (A ≤ B)
print("\n1. Числа от A до B (A ≤ B):")
A = int(input("Введите число A: "))
B = int(input("Введите число B (A ≤ B): "))
print("Числа от A до B:")
for i in range(A, B + 1):
    print(i, end=" ")

# 2. Вывести числа от A до B в порядке возрастания или убывания
print("\n\n2. Числа от A до B в нужном порядке:")
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
print("Результат:")
if A < B:
    for i in range(A, B + 1):
        print(i, end=" ")
else:
    for i in range(A, B - 1, -1):
        print(i, end=" ")

# 3. Нечётные числа от A до B в порядке убывания (A > B)
print("\n\n3. Нечётные числа от A до B в порядке убывания (A > B):")
A = int(input("Введите число A (большее): "))
B = int(input("Введите число B (меньшее): "))
print("Нечётные числа в порядке убывания:")
for i in range(A, B - 1, -1):
    if i % 2 != 0:
        print(i, end=" ")

# 4. Сумма N чисел (минимальное количество переменных)
print("\n\n4. Сумма N чисел:")
N = int(input("Введите количество чисел N: "))
total = 0
for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    total += num
print(f"Сумма всех чисел: {total}")

# 5. Сумма 1*3 + 2*3 + ... + n*3
print("\n5. Сумма ряда 1*3 + 2*3 + ... + n*3:")
n = int(input("Введите натуральное n: "))
sum_result = 0
for i in range(1, n + 1):
    sum_result += i * 3
print(f"Сумма ряда: {sum_result}")

# 6. Факториал n без использования math
print("\n6. Факториал n (без math):")
n = int(input("Введите натуральное n: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# 7. Сумма факториалов 1! + 2! + ... + n! (один цикл)
print("\n7. Сумма факториалов 1! + 2! + ... + n! (один цикл):")
n = int(input("Введите натуральное n: "))
total_sum = 0
current_factorial = 1
for i in range(1, n + 1):
    current_factorial *= i
    total_sum += current_factorial
print(f"Сумма факториалов: {total_sum}")

# 8. Лесенка из чисел (n ≤ 9)
print("\n8. Лесенка из чисел:")
n = int(input("Введите n (≤ 9): "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 9. Сумма N чисел Фибоначчи
print("\n9. Сумма N чисел Фибоначчи:")
N = int(input("Введите количество чисел N: "))
if N <= 0:
    print("Сумма: 0")
elif N == 1:
    print("Сумма: 0")
elif N == 2:
    print("Сумма: 1")
else:
    a, b = 0, 1
    fib_sum = 1  # 0 + 1 для первых двух чисел
    count = 2  # уже учли 0 и 1

    while count < N:
        a, b = b, a + b
        fib_sum += b
        count += 1

    print(f"Сумма первых {N} чисел Фибоначчи: {fib_sum}")

# 10. Сумма N чисел Фибоначчи начиная с K-го (один цикл)
print("\n10. Сумма N чисел Фибоначчи начиная с K-го (один цикл):")
N = int(input("Введите количество чисел N: "))
K = int(input("Введите начальный номер K: "))

if N <= 0:
    print("Сумма: 0")
else:
    # Находим K-е число Фибоначчи
    if K == 1:
        a, b = 0, 1
    elif K == 2:
        a, b = 1, 1
    else:
        a, b = 0, 1
        for _ in range(K - 2):
            a, b = b, a + b

    # Суммируем N чисел начиная с K-го
    fib_sum = b
    count = 1

    while count < N:
        a, b = b, a + b
        fib_sum += b
        count += 1

    print(f"Сумма {N} чисел Фибоначчи с {K}-го: {fib_sum}")

print("\n" + "=" * 50)
print("Все задачи выполнены!")
print("=" * 50)