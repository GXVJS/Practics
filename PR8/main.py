import random

print("=" * 50)
print("практическая номер 8")
print("=" * 50)

# Вариант 1.1: Сумма и число положительных элементов над главной диагональю
print("\nВар.1.1: Сумма и число положительных элементов над главной диагональю")

def create_square_matrix(N):
    """Создание квадратной матрицы NxN с ручным вводом"""
    matrix = []
    print(f"Введите элементы матрицы {N}x{N} построчно:")
    for i in range(N):
        row = []
        print(f"Строка {i + 1}: ", end="")
        elements = input().split()
        for elem in elements:
            row.append(int(elem))
        # Если введено недостаточно элементов, дополняем нулями
        while len(row) < N:
            row.append(0)
        matrix.append(row[:N])  # Берем только N элементов
    return matrix

def print_matrix(matrix, title="Матрица"):
    """Красивый вывод матрицы"""
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(f"{elem:4}" for elem in row))


N = int(input("Введите размер квадратной матрицы N: "))
A = create_square_matrix(N)
print_matrix(A)

# Вычисляем сумму и количество положительных элементов над главной диагональю
sum_positive = 0
count_positive = 0
for i in range(N):
    for j in range(N):
        if j > i:  # Элементы над главной диагональю (j > i)
            if A[i][j] > 0:
                sum_positive += A[i][j]
                count_positive += 1

print(f"\nЭлементы над главной диагональю:")
for i in range(N):
    for j in range(N):
        if j > i:
            print(f"A[{i + 1},{j + 1}] = {A[i][j]}", end="; ")

print(f"\n\nЧисло положительных элементов над главной диагональю: {count_positive}")
print(f"Сумма положительных элементов над главной диагональю: {sum_positive}")

# Вариант 2.1: Проверка магического квадрата
print("\n\nВар.2.1: Проверка магического квадрата")


def is_magic_square(matrix):
    """Проверка, является ли матрица магическим квадратом"""
    n = len(matrix)

    # Вычисляем сумму первой строки (эталон)
    magic_sum = sum(matrix[0])

    # Проверяем суммы всех строк
    for i in range(1, n):
        if sum(matrix[i]) != magic_sum:
            return False

    # Проверяем суммы всех столбцов
    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != magic_sum:
            return False

    # Проверяем сумму главной диагонали
    diag1_sum = sum(matrix[i][i] for i in range(n))
    if diag1_sum != magic_sum:
        return False

    # Проверяем сумму побочной диагонали
    diag2_sum = sum(matrix[i][n - 1 - i] for i in range(n))
    if diag2_sum != magic_sum:
        return False

    return True

print("Введите размер квадратной матрицы n: ")
n = int(input())
matrix = create_square_matrix(n)
print_matrix(matrix, "Матрица для проверки")

if is_magic_square(matrix):
    print("✓ Матрица является магическим квадратом")
    magic_sum = sum(matrix[0])
    print(f"Магическая сумма: {magic_sum}")
else:
    print("✗ Матрица НЕ является магическим квадратом")

# Вариант 3.1: Проверка симметричности матрицы
print("\n\nВар.3.1: Проверка симметричности матрицы")

def is_symmetric(matrix):
    """Проверка, является ли матрица симметричной относительно главной диагонали"""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):  # Проверяем только элементы выше диагонали
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

print("Введите размер квадратной матрицы n: ")
n = int(input())
matrix = create_square_matrix(n)
print_matrix(matrix, "Матрица для проверки симметричности")

if is_symmetric(matrix):
    print("✓ Матрица симметрична относительно главной диагонали")
else:
    print("✗ Матрица НЕ симметрична относительно главной диагонали")

# Вариант 4.1: Строки с наибольшей и наименьшей суммой элементов
print("\n\nВар.4.1: Строки с наибольшей и наименьшей суммой элементов")


def create_rectangular_matrix(n, m):
    """Создание прямоугольной матрицы n x m"""
    matrix = []
    print(f"Введите элементы матрицы {n}x{m} построчно:")
    for i in range(n):
        row = []
        print(f"Строка {i + 1}: ", end="")
        elements = input().split()
        for elem in elements:
            row.append(int(elem))
        while len(row) < m:
            row.append(0)
        matrix.append(row[:m])
    return matrix

print("Введите размеры прямоугольной матрицы:")
n = int(input("Количество строк n: "))
m = int(input("Количество столбцов m: "))
matrix = create_rectangular_matrix(n, m)
print_matrix(matrix, "Исходная матрица")

# Находим суммы строк
row_sums = []
for i in range(n):
    row_sum = sum(matrix[i])
    row_sums.append(row_sum)
    print(f"Строка {i + 1}: сумма = {row_sum}")

# Находим строку с максимальной и минимальной суммой
max_sum_index = row_sums.index(max(row_sums))
min_sum_index = row_sums.index(min(row_sums))

print(f"\nСтрока с наибольшей суммой ({row_sums[max_sum_index]}): строка {max_sum_index + 1}")
print(f"Элементы: {matrix[max_sum_index]}")
print(f"\nСтрока с наименьшей суммой ({row_sums[min_sum_index]}): строка {min_sum_index + 1}")
print(f"Элементы: {matrix[min_sum_index]}")

# Вариант 5.1: Сортировка элементов каждой строки по возрастанию
print("\n\nВар.5.1: Сортировка элементов каждой строки по возрастанию")

print("Введите размеры матрицы:")
n = int(input("Количество строк n: "))
m = int(input("Количество столбцов m: "))
matrix = create_rectangular_matrix(n, m)
print_matrix(matrix, "Исходная матрица")

# Сортируем каждую строку
sorted_matrix = [sorted(row) for row in matrix]

print_matrix(sorted_matrix, "Матрица после сортировки строк")

# Вариант 6.1: Максимальный в строке и минимальный в столбце
print("\n\nВар.6.1: Максимальный в строке и минимальный в столбце")


def create_int_square_matrix(N):
    """Создание целочисленной квадратной матрицы"""
    matrix = []
    print(f"Введите элементы целочисленной матрицы {N}x{N} построчно:")
    for i in range(N):
        row = []
        print(f"Строка {i + 1}: ", end="")
        elements = input().split()
        for elem in elements:
            row.append(int(elem))
        while len(row) < N:
            row.append(0)
        matrix.append(row[:N])
    return matrix

N = int(input("Введите размер квадратной матрицы N: "))
matrix = create_int_square_matrix(N)
print_matrix(matrix, "Исходная матрица")

print("\nНаибольшие элементы в каждой строке:")
for i in range(N):
    max_in_row = max(matrix[i])
    max_index = matrix[i].index(max_in_row)
    print(f"Строка {i + 1}: {max_in_row} (индекс {max_index})")

print("\nНаименьшие элементы в каждом столбце:")
for j in range(N):
    min_in_col = min(matrix[i][j] for i in range(N))
    min_index = min(range(N), key=lambda i: matrix[i][j])
    print(f"Столбец {j + 1}: {min_in_col} (в строке {min_index + 1})")

# Вариант 7.1: Восстановление симметричной матрицы из верхнего треугольника
print("\nВар.7.1: Восстановление симметричной матрицы из верхнего треугольника")

def restore_symmetric_matrix(arr, n):
    """
    Восстанавливает симметричную матрицу n×n из одномерного массива,
    содержащего элементы верхнего треугольника (включая диагональ)
    Элементы читаются построчно
    """
    matrix = [[0] * n for _ in range(n)]
    idx = 0

    # Заполняем верхний треугольник (включая диагональ)
    for i in range(n):
        for j in range(i, n):
            if idx < len(arr):
                matrix[i][j] = arr[idx]
                idx += 1

    # Заполняем нижний треугольник по симметрии
    for i in range(n):
        for j in range(i):
            matrix[i][j] = matrix[j][i]

    return matrix
print("Введите размер матрицы n: ")
n = int(input())

# Вычисляем сколько элементов в верхнем треугольнике (включая диагональ)
elements_count = n * (n + 1) // 2
print(f"Введите {elements_count} элементов верхнего треугольника (по строкам):")

arr = []
for i in range(elements_count):
    elem = float(input(f"Элемент {i + 1}: "))
    arr.append(elem)

# Восстанавливаем матрицу
matrix = restore_symmetric_matrix(arr, n)

print("\nВосстановленная симметричная матрица:")
for i in range(n):
    for j in range(n):
        print(f"{matrix[i][j]:6.1f}", end=" ")
    print()

# Вариант 8.1: Деление элементов строки на диагональный элемент
print("\n\nВар.8.1: Деление элементов строки на диагональный элемент")


def divide_row_by_diagonal():
    n = int(input("Введите порядок матрицы n: "))
    k = int(input(f"Введите номер строки k (1-{n}): ")) - 1

    print(f"Введите элементы матрицы {n}x{n}:")
    matrix = []
    for i in range(n):
        row = []
        print(f"Строка {i + 1}: ", end="")
        elements = input().split()
        for elem in elements:
            row.append(float(elem))
        while len(row) < n:
            row.append(0.0)
        matrix.append(row[:n])

    print("\nИсходная матрица:")
    for row in matrix:
        print(" ".join(f"{x:6.2f}" for x in row))

    # Проверяем, что k в допустимых пределах
    if 0 <= k < n:
        diagonal_elem = matrix[k][k]
        print(f"\nДиагональный элемент в строке {k + 1}: {diagonal_elem}")

        if diagonal_elem != 0:
            # Делим элементы k-й строки на диагональный элемент
            for j in range(n):
                matrix[k][j] /= diagonal_elem

            print(f"\nМатрица после деления {k + 1}-й строки на {diagonal_elem}:")
            for row in matrix:
                print(" ".join(f"{x:8.4f}" for x in row))
        else:
            print("Ошибка: диагональный элемент равен 0, деление невозможно")
    else:
        print("Ошибка: некорректный номер строки")
divide_row_by_diagonal()

# Вариант 9.1: Элементы, кратные k
print("\n\nВар.9.1: Элементы, кратные k")


def find_multiples():
    n = int(input("Введите размер квадратной матрицы: "))
    k = int(input("Введите число k: "))

    print(f"Введите целочисленные элементы матрицы {n}x{n}:")
    matrix = []
    for i in range(n):
        row = []
        print(f"Строка {i + 1}: ", end="")
        elements = input().split()
        for elem in elements:
            row.append(int(elem))
        while len(row) < n:
            row.append(0)
        matrix.append(row[:n])

    print("\nИсходная матрица:")
    for row in matrix:
        print(" ".join(f"{x:4}" for x in row))

    # Находим элементы, кратные k
    multiples = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] % k == 0 and matrix[i][j] != 0:
                multiples.append(matrix[i][j])

    if multiples:
        count = len(multiples)
        max_multiple = max(multiples)
        print(f"\nЧисло элементов, кратных {k}: {count}")
        print(f"Элементы, кратные {k}: {multiples}")
        print(f"Наибольший из элементов, кратных {k}: {max_multiple}")
    else:
        print(f"\nЭлементов, кратных {k}, не найдено")
find_multiples()

# Вариант 10.1: Максимальный элемент в упорядоченных строках
print("\n\nВар.10.1: Максимальный элемент в упорядоченных строках")

def max_in_ordered_rows():
    n = int(input("Введите количество строк матрицы: "))
    m = int(input("Введите количество столбцов матрицы: "))

    print(f"Введите элементы матрицы {n}x{m}:")
    matrix = []
    for i in range(n):
        row = []
        print(f"Строка {i + 1}: ", end="")
        elements = input().split()
        for elem in elements:
            row.append(float(elem))
        while len(row) < m:
            row.append(0.0)
        matrix.append(row[:m])

    print("\nИсходная матрица:")
    for row in matrix:
        print(" ".join(f"{x:6.2f}" for x in row))

    def is_ordered(arr):
        """Проверяет, упорядочен ли массив по возрастанию или по убыванию"""
        if len(arr) <= 1:
            return True
        # Проверка на возрастание
        increasing = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
        # Проверка на убывание
        decreasing = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
        return increasing or decreasing

    # Находим упорядоченные строки
    ordered_rows_max = []
    for i in range(n):
        if is_ordered(matrix[i]):
            row_max = max(matrix[i])
            ordered_rows_max.append(row_max)
            print(f"Строка {i + 1} упорядочена, максимальный элемент: {row_max}")
        else:
            print(f"Строка {i + 1} не упорядочена")

    if ordered_rows_max:
        overall_max = max(ordered_rows_max)
        print(f"\nМаксимальный среди всех элементов упорядоченных строк: {overall_max}")
    else:
        print("\nНет упорядоченных строк")
max_in_ordered_rows()

# Вариант 11.1: Сумма элементов строки с минимальным элементом
print("\n\nВар.11.1: Сумма элементов строки с минимальным элементом")

def sum_row_with_min_element():
    n = int(input("Введите порядок матрицы n: "))

    print(f"Введите действительные элементы матрицы {n}x{n}:")
    matrix = []
    for i in range(n):
        row = []
        print(f"Строка {i + 1}: ", end="")
        elements = input().split()
        for elem in elements:
            row.append(float(elem))
        while len(row) < n:
            row.append(0.0)
        matrix.append(row[:n])

    print("\nИсходная матрица:")
    for row in matrix:
        print(" ".join(f"{x:8.2f}" for x in row))

    # Находим минимальный элемент и его строку
    min_value = float('inf')
    min_row_index = -1

    for i in range(n):
        for j in range(n):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_row_index = i

    print(f"\nМинимальный элемент: {min_value}")
    print(f"Находится в строке {min_row_index + 1}")

    # Вычисляем сумму элементов этой строки
    row_sum = sum(matrix[min_row_index])
    print(f"Сумма элементов строки {min_row_index + 1}: {row_sum}")

    print(f"Элементы строки {min_row_index + 1}: {matrix[min_row_index]}")
sum_row_with_min_element()

# Вариант 12.1: Нахождение k, где k-я строка совпадает с k-м столбцом
print("\nВар.12.1: Поиск строк, совпадающих со столбцами")

def find_matching_rows_columns():
    n = int(input("Введите размер квадратной матрицы: "))

    print(f"Введите элементы матрицы {n}x{n}:")
    matrix = []
    for i in range(n):
        row = []
        print(f"Строка {i + 1}: ", end="")
        elements = input().split()
        for elem in elements:
            row.append(float(elem))
        while len(row) < n:
            row.append(0.0)
        matrix.append(row[:n])

    print("\nИсходная матрица:")
    for i in range(n):
        print(f"Строка {i + 1}: ", end="")
        for j in range(n):
            print(f"{matrix[i][j]:6.2f}", end=" ")
        print()

    # Проверяем, какие строки совпадают с соответствующими столбцами
    matching_indices = []
    for k in range(n):
        row_matches_column = True
        for i in range(n):
            if matrix[k][i] != matrix[i][k]:
                row_matches_column = False
                break

        if row_matches_column:
            matching_indices.append(k + 1)  # +1 для отображения с 1, а не с 0

    if matching_indices:
        print(f"\nНайдены строки, совпадающие со столбцами: {matching_indices}")
        for k in matching_indices:
            print(f"Строка {k}: {matrix[k - 1]}")
    else:
        print("\nНет строк, совпадающих с соответствующими столбцами")

find_matching_rows_columns()

# Вариант 13.1: Наименьший элемент каждой четной строки
print("\n\nВар.13.1: Наименьший элемент каждой четной строки")


def min_in_even_rows():
    M = int(input("Введите количество строк M: "))
    N = int(input("Введите количество столбцов N: "))

    print(f"Введите элементы матрицы {M}x{N}:")
    A = []
    for i in range(M):
        row = []
        print(f"Строка {i + 1}: ", end="")
        elements = input().split()
        for elem in elements:
            row.append(float(elem))
        while len(row) < N:
            row.append(0.0)
        A.append(row[:N])

    print("\nИсходная матрица:")
    for i in range(M):
        print(f"Строка {i + 1}: ", end="")
        for j in range(N):
            print(f"{A[i][j]:6.2f}", end=" ")
        print()

    print("\nНаименьшие элементы четных строк:")
    for i in range(M):
        if (i + 1) % 2 == 0:  # Четные строки (нумерация с 1)
            min_val = min(A[i])
            min_index = A[i].index(min_val)
            print(f"Строка {i + 1}: наименьший элемент = {min_val} (индекс {min_index + 1})")

min_in_even_rows()

# Вариант 14.1: Перестановка строк
print("\n\nВар.14.1: Перестановка строки с максимальным элементом на главной диагонали")


def swap_max_diagonal_row():
    n = int(input("Введите размер квадратной матрицы: "))
    m = int(input("Введите номер строки m для обмена (1-{n}): ".format(n=n)))

    print(f"Введите элементы матрицы {n}x{n}:")
    matrix = []
    for i in range(n):
        row = []
        print(f"Строка {i + 1}: ", end="")
        elements = input().split()
        for elem in elements:
            row.append(float(elem))
        while len(row) < n:
            row.append(0.0)
        matrix.append(row[:n])

    print("\nИсходная матрица:")
    for i in range(n):
        for j in range(n):
            print(f"{matrix[i][j]:6.2f}", end=" ")
        print()

    # Находим строку с максимальным элементом на главной диагонали
    max_diag_val = matrix[0][0]
    max_diag_row = 0

    for i in range(n):
        if matrix[i][i] > max_diag_val:
            max_diag_val = matrix[i][i]
            max_diag_row = i

    print(f"\nМаксимальный элемент на главной диагонали: {max_diag_val}")
    print(f"Находится в строке {max_diag_row + 1}")

    if m < 1 or m > n:
        print("Некорректный номер строки m")
        return

    # Переставляем строки
    if max_diag_row + 1 != m:
        matrix[max_diag_row], matrix[m - 1] = matrix[m - 1], matrix[max_diag_row]
        print(f"\nМатрица после перестановки строки {max_diag_row + 1} и строки {m}:")
        for i in range(n):
            for j in range(n):
                print(f"{matrix[i][j]:8.2f}", end=" ")
            print()
    else:
        print(f"\nМаксимальный элемент уже находится в строке {m}, перестановка не требуется")

swap_max_diagonal_row()

# Вариант 15.1: Умножение строк с элементом c на d
print("\n\nВар.15.1: Умножение строк с элементом c на d")


def multiply_rows_with_element():
    M = int(input("Введите количество строк M: "))
    N = int(input("Введите количество столбцов N: "))
    c = float(input("Введите число c: "))
    d = float(input("Введите число d: "))

    print(f"Введите элементы матрицы R {M}x{N}:")
    R = []
    for i in range(M):
        row = []
        print(f"Строка {i + 1}: ", end="")
        elements = input().split()
        for elem in elements:
            row.append(float(elem))
        while len(row) < N:
            row.append(0.0)
        R.append(row[:N])

    print("\nИсходная матрица:")
    for i in range(M):
        for j in range(N):
            print(f"{R[i][j]:6.2f}", end=" ")
        print()

    # Находим строки, содержащие элемент c
    rows_with_c = []
    for i in range(M):
        if c in R[i]:
            rows_with_c.append(i)

    if rows_with_c:
        print(f"\nСтроки, содержащие элемент {c}: {[i + 1 for i in rows_with_c]}")

        # Умножаем элементы этих строк на d
        transformed = [row[:] for row in R]
        for i in rows_with_c:
            for j in range(N):
                transformed[i][j] *= d

        print(f"\nМатрица после умножения строк {[i + 1 for i in rows_with_c]} на {d}:")
        for i in range(M):
            if i in rows_with_c:
                print(f"Строка {i + 1} (измененная): ", end="")
            else:
                print(f"Строка {i + 1}: ", end="")
            for j in range(N):
                print(f"{transformed[i][j]:8.2f}", end=" ")
            print()
    else:
        print(f"\nНет строк, содержащих элемент {c}")

multiply_rows_with_element()
