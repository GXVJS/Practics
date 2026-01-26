zadanie = int(input("Введите номер задания"))
if zadanie == 1:
    def restore_symmetric_matrix(triangle_array):
        #n*(n+1)/2 = len(triangle_array)
        #n^2 + n - 2*len = 0
        length = len(triangle_array)
        #размер матрицы
        n = 0
        for i in range(1, 100):  # практический подход
            if i * (i + 1) // 2 == length:
                n = i
                break
        if n == 0:
            print("Ошибка: невозможно определить размер матрицы!")
            return None
        print(f"Размер матрицы: {n}x{n}")
        # Создаем нулевую матрицу n x n
        matrix = [[0] * n for _ in range(n)]
        # Восстанавление матрицы
        index = 0
        for i in range(n):
            for j in range(i, n):  # только верхний треугольник (включая диагональ)
                matrix[i][j] = triangle_array[index]
                matrix[j][i] = triangle_array[index]  # симметричный элемент
                index += 1
        return matrix
    #Ввод от пользователя
    print("\nВвод от пользователя:")
    try:
        # Ввод элементов верхнего треугольника
        input_str = input("Введите элементы верхнего треугольника через пробел: ")
        triangle_input = list(map(int, input_str.split()))

        matrix_input = restore_symmetric_matrix(triangle_input)
        if matrix_input:
            print("Восстановленная матрица:")
            for i, row in enumerate(matrix_input):
                print(f"Строка {i + 1}: {row}")
    except ValueError:
        print("Ошибка: введите целые числа через пробел!")

elif zadanie == 2:
    def simple_matrix_processor():
        print("=" * 50)
        print("ОБРАБОТКА КВАДРАТНОЙ МАТРИЦЫ")
        print("=" * 50)

        # Ввод размера
        while True:
            try:
                n = int(input("\nВведите размер матрицы (n): "))
                if n > 0:
                    break
                print("Размер должен быть положительным!")
            except:
                print("Введите целое число!")

        # Ввод матрицы
        print(f"\nВведите матрицу {n}×{n} построчно:")
        print("Пример: для строки '1 2 3' введите три числа через пробел")

        matrix = []
        for i in range(n):
            while True:
                try:
                    row_input = input(f"Строка {i + 1}: ")
                    numbers = [float(x) for x in row_input.split()]

                    if len(numbers) == n:
                        matrix.append(numbers)
                        break
                    else:
                        print(f"Ошибка! Нужно {n} чисел, а введено {len(numbers)}")
                except:
                    print("Ошибка ввода! Используйте формат: '1.5 2 3.7'")

        # Показываем матрицу
        print(f"\nВаша матрица {n}×{n}:")
        for row in matrix:
            print("  " + " ".join(f"{x:8.2f}" for x in row))

        # Диагональные элементы
        print("\nДиагональные элементы:")
        diagonal = []
        for i in range(n):
            diag_element = matrix[i][i]
            diagonal.append(diag_element)
            print(f"  a[{i + 1}][{i + 1}] = {diag_element}")

        # След матрицы
        trace = sum(diagonal)
        print(f"\nСлед матрицы (сумма диагонали) = {trace}")

        # Преобразование
        if trace == 0:
            print("\nНевозможно выполнить преобразование: след равен 0!")
            return

        # Создаем новую матрицу
        new_matrix = []
        for i in range(n):
            if (i + 1) % 2 == 0:  # четные строки
                new_row = [x / trace for x in matrix[i]]
                new_matrix.append(new_row)
                print(f"\nСтрока {i + 1} (четная) разделена на {trace}:")
            else:  # нечетные строки
                new_matrix.append(matrix[i][:])
                print(f"\nСтрока {i + 1} (нечетная) без изменений:")

            # Показываем текущую строку
            print("  " + " ".join(f"{x:8.4f}" for x in new_matrix[i]))
    # Быстрый запуск
    simple_matrix_processor()