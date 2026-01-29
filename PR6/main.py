print("=" * 50)
print("Практическая 6")
print("=" * 50)

# Вариант 1.1: Найти максимальный элемент массива
print("\nВар.1.1: Поиск максимального элемента массива")
n = int(input("Введите количество элементов массива N: "))
arr = []
print(f"Введите {n} целых чисел:")
for i in range(n):
    num = int(input(f"Элемент {i + 1}: "))
    arr.append(num)

max_element = max(arr)
print(f"Массив: {arr}")
print(f"Максимальный элемент: {max_element}")

# Вариант 2.1: Найти минимальный элемент и его индекс
print("\n\nВар.2.1: Поиск минимального элемента и его индекса")
n = int(input("Введите количество элементов массива N: "))
arr = []
print(f"Введите {n} целых чисел:")
for i in range(n):
    num = int(input(f"Элемент {i + 1}: "))
    arr.append(num)

min_element = min(arr)
min_index = arr.index(min_element)  # Находим первый индекс минимального элемента

print(f"Массив: {arr}")
print(f"Минимальный элемент: {min_element}")
print(f"Индекс минимального элемента: {min_index}")

# Вариант 3.1: Сумма элементов с нечетными индексами
print("\n\nВар.3.1: Сумма элементов с нечетными индексами")
n = int(input("Введите количество элементов массива n: "))
D = []
print(f"Введите {n} чисел:")
for i in range(n):
    num = float(input(f"D[{i}]: "))
    D.append(num)

odd_sum = 0
for i in range(1, n, 2):  # Индексы 1, 3, 5, ...
    odd_sum += D[i]

print(f"Массив D: {D}")
print(f"Сумма элементов с нечетными индексами: {odd_sum}")

# Вариант 4.1: Максимальный элемент и его порядковый номер
print("\n\nВар.4.1: Максимальный элемент и его порядковый номер")
arr = []
n = int(input("Введите количество элементов массива: "))
print(f"Введите {n} целых чисел:")
for i in range(n):
    num = int(input(f"Элемент {i + 1}: "))
    arr.append(num)

max_val = max(arr)
max_index = arr.index(max_val)

print(f"Массив: {arr}")
print(f"Максимальный элемент: {max_val}")
print(f"Порядковый номер (индекс): {max_index}")

# Вариант 5.1: Пары отрицательных чисел, стоящих рядом
print("\n\nВар.5.1: Пары отрицательных чисел, стоящих рядом")
arr = []
print("Введите 10 целых чисел:")
for i in range(10):
    num = int(input(f"Элемент {i + 1}: "))
    arr.append(num)

print(f"Массив: {arr}")
print("Пары отрицательных чисел, стоящих рядом:")

found_pairs = False
for i in range(9):  # Проверяем с 0 до 8 индекса (чтобы i+1 было в пределах)
    if arr[i] < 0 and arr[i + 1] < 0:
        print(f"({arr[i]}, {arr[i + 1]}) на позициях {i} и {i + 1}")
        found_pairs = True

if not found_pairs:
    print("Пар отрицательных чисел рядом не найдено")

# Вариант 6.1: Сравнение элементов с максимальным
print("\n\nВар.6.1: Сравнение элементов с максимальным")
arr = []
print("Введите 10 целых чисел:")
for i in range(10):
    num = int(input(f"Элемент {i + 1}: "))
    arr.append(num)

max_val = max(arr)
less_count = 0
greater_count = 0

for num in arr:
    if num < max_val:
        less_count += 1
    elif num > max_val:
        greater_count += 1

print(f"Массив: {arr}")
print(f"Максимальный элемент: {max_val}")
print(f"Количество элементов меньше максимального: {less_count}")
print(f"Количество элементов больше максимального: {greater_count}")

# Вариант 7.1: Сумма четных и произведение нечетных элементов
print("\n\nВар.7.1: Сумма четных и произведение нечетных элементов")
arr = []
n = int(input("Введите количество элементов массива: "))
print(f"Введите {n} целых чисел:")
for i in range(n):
    num = int(input(f"Элемент {i + 1}: "))
    arr.append(num)

even_sum = 0  # Сумма элементов с четными индексами (0, 2, 4, ...)
odd_product = 1  # Произведение элементов с нечетными индексами (1, 3, 5, ...)

has_odd_indices = False  # Флаг, есть ли элементы с нечетными индексами

for i in range(n):
    if i % 2 == 0:  # Четный индекс
        even_sum += arr[i]
    else:  # Нечетный индекс
        odd_product *= arr[i]
        has_odd_indices = True

print(f"Массив: {arr}")
print(f"Сумма элементов с четными индексами: {even_sum}")

if has_odd_indices:
    print(f"Произведение элементов с нечетными индексами: {odd_product}")
else:
    print("Элементов с нечетными индексами нет")

# Вариант 8.1: Сумма и произведение элементов списка
print("\n\nВар.8.1: Сумма и произведение элементов списка")
arr = []
n = int(input("Введите количество элементов в списке: "))
print(f"Введите {n} чисел:")
for i in range(n):
    num = float(input(f"Элемент {i + 1}: "))
    arr.append(num)

sum_elements = sum(arr)
product_elements = 1
for num in arr:
    product_elements *= num

print(f"Список: {arr}")
print(f"Сумма элементов: {sum_elements}")
print(f"Произведение элементов: {product_elements}")


# Вариант 9.1: Минимальный по модулю и обратный порядок
print("\n\nВар.9.1: Минимальный по модулю и обратный порядок")
n = int(input("Введите количество элементов N: "))
arr = []
print(f"Введите {n} вещественных чисел:")
for i in range(n):
    num = float(input(f"Элемент {i + 1}: "))
    arr.append(num)

# Находим минимальный по модулю
min_abs = min(arr, key=abs)
print(f"Массив: {arr}")
print(f"Минимальный по модулю элемент: {min_abs}")
print(f"Массив в обратном порядке: {arr[::-1]}")

# Вариант 10.1: Поиск повторяющихся элементов
print("\n\nВар.10.1: Поиск повторяющихся элементов")
arr = []
n = int(input("Введите количество элементов в списке: "))
print(f"Введите {n} элементов:")
for i in range(n):
    element = input(f"Элемент {i + 1}: ")
    arr.append(element)

# Ищем дубликаты
seen = set()
duplicates = set()
for element in arr:
    if element in seen:
        duplicates.add(element)
    else:
        seen.add(element)

if duplicates:
    print(f"Повторяющиеся элементы: {list(duplicates)}")
else:
    print("Повторяющихся элементов нет")

# Вариант 11.1: Наибольший четный элемент
print("\n\nВар.11.1: Наибольший четный элемент")
arr = []
n = int(input("Введите количество элементов в списке: "))
print(f"Введите {n} целых чисел:")
for i in range(n):
    num = int(input(f"Элемент {i + 1}: "))
    arr.append(num)

even_numbers = [num for num in arr if num % 2 == 0]
if even_numbers:
    max_even = max(even_numbers)
    print(f"Список: {arr}")
    print(f"Наибольший четный элемент: {max_even}")
else:
    print(f"Список: {arr}")
    print("Четных элементов нет")

# Вариант 12.1: Наименьший нечетный элемент
print("\n\nВар.12.1: Наименьший нечетный элемент")
arr = []
n = int(input("Введите количество элементов в списке: "))
print(f"Введите {n} целых чисел:")
for i in range(n):
    num = int(input(f"Элемент {i + 1}: "))
    arr.append(num)

odd_numbers = [num for num in arr if num % 2 != 0]
if odd_numbers:
    min_odd = min(odd_numbers)
    print(f"Список: {arr}")
    print(f"Наименьший нечетный элемент: {min_odd}")
else:
    print(f"Список: {arr}")
    print("Нечетных элементов нет")

# Вариант 13.1: Поиск одинаковых элементов и их индексов
print("\n\nВар.13.1: Поиск одинаковых элементов и их индексов")
arr = []
n = int(input("Введите количество элементов массива: "))
print(f"Введите {n} целых чисел:")
for i in range(n):
    num = int(input(f"Элемент {i + 1}: "))
    arr.append(num)

print(f"Массив: {arr}")

# Словарь для хранения индексов каждого элемента
element_indices = {}
for i, num in enumerate(arr):
    if num not in element_indices:
        element_indices[num] = []
    element_indices[num].append(i)

# Выводим элементы, которые встречаются более 1 раза
found_duplicates = False
for num, indices in element_indices.items():
    if len(indices) > 1:
        print(f"Элемент {num} встречается на позициях: {indices}")
        found_duplicates = True

if not found_duplicates:
    print("Одинаковых элементов нет")

# Вариант 14.1: Поменять местами максимальный и минимальный элементы
print("\n\nВар.14.1: Поменять местами максимальный и минимальный элементы")
arr = []
n = int(input("Введите количество элементов массива: "))
print(f"Введите {n} чисел:")
for i in range(n):
    num = float(input(f"Элемент {i + 1}: "))
    arr.append(num)

if n > 0:
    original_arr = arr.copy()
    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))

    # Меняем местами
    arr[max_index], arr[min_index] = arr[min_index], arr[max_index]

    print(f"Исходный массив: {original_arr}")
    print(f"Максимальный элемент был на позиции {max_index}")
    print(f"Минимальный элемент был на позиции {min_index}")
    print(f"Массив после замены: {arr}")
else:
    print("Массив пустой")

# Вариант 15.1: Вывод всех повторяющихся значений
print("\n\nВар.15.1: Вывод всех повторяющихся значений")
arr = []
n = int(input("Введите количество элементов в списке: "))
print(f"Введите {n} элементов:")
for i in range(n):
    element = input(f"Элемент {i + 1}: ")
    arr.append(element)

# Считаем частоту каждого элемента
frequency = {}
for element in arr:
    frequency[element] = frequency.get(element, 0) + 1

# Находим элементы, которые встречаются более 1 раза
duplicates = [element for element, count in frequency.items() if count > 1]

print(f"Список: {arr}")
if duplicates:
    print(f"Повторяющиеся значения: {duplicates}")
else:
    print("Повторяющихся значений нет")
