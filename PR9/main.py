import os
import sys
def read_matrix_from_file(filename):
    """
    Чтение матрицы из файла.
    Формат файла:
    - Первая строка: размер матрицы N
    - Следующие N строк: элементы матрицы, разделенные пробелами
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                return None, "Файл пуст"

            # Читаем размер матрицы
            try:
                n = int(lines[0].strip())
            except ValueError:
                return None, "Некорректный размер матрицы в первой строке"

            # Проверяем, что достаточно строк
            if len(lines) < n + 1:
                return None, f"Недостаточно строк в файле. Ожидалось {n + 1}, есть {len(lines)}"

            matrix = []
            for i in range(1, n + 1):
                try:
                    row = list(map(float, lines[i].strip().split()))
                    if len(row) != n:
                        return None, f"В строке {i} неверное количество элементов. Ожидалось {n}, получено {len(row)}"
                    matrix.append(row)
                except ValueError:
                    return None, f"Некорректные данные в строке {i + 1}"

            return matrix, None

    except FileNotFoundError:
        return None, f"Файл {filename} не найден"
    except Exception as e:
        return None, f"Ошибка при чтении файла: {str(e)}"


def read_triangle_array_from_file(filename):
    """
    Чтение одномерного массива (верхнего треугольника) из файла.
    Формат файла: все элементы в одной строке, разделенные пробелами
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                return None, "Файл пуст"

            try:
                # Пробуем прочитать как несколько строк
                lines = file.readlines()
                if lines:
                    # Если есть несколько строк, читаем первую
                    triangle_array = list(map(float, lines[0].strip().split()))
                else:
                    # Или читаем весь файл как одну строку
                    file.seek(0)
                    content = file.read().strip()
                    triangle_array = list(map(float, content.split()))

                return triangle_array, None
            except ValueError:
                return None, "Некорректные данные в файле (ожидались числа)"

    except FileNotFoundError:
        return None, f"Файл {filename} не найден"
    except Exception as e:
        return None, f"Ошибка при чтении файла: {str(e)}"


def task1_restore_symmetric_matrix(triangle_array, output_file):
    """
    Задача 1: Восстановление симметричной матрицы
    """
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("ЗАДАЧА 1: Восстановление симметричной матрицы\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"Исходный одномерный массив (верхний треугольник):\n")
        f.write(f"{triangle_array}\n\n")

        # Находим размер матрицы n из уравнения: n*(n+1)/2 = len(triangle_array)
        length = len(triangle_array)

        # Решаем квадратное уравнение n^2 + n - 2*length = 0
        n = 0
        for i in range(1, 100):  # практический поиск
            if i * (i + 1) // 2 == length:
                n = i
                break

        if n == 0:
            f.write("ОШИБКА: Невозможно определить размер матрицы!\n")
            f.write(f"Количество элементов в массиве: {length}\n")
            f.write("Для матрицы n×n должно быть n*(n+1)/2 элементов\n")
            return None

        f.write(f"Определен размер матрицы: {n}×{n}\n")
        f.write(f"(n*(n+1)/2 = {n}*{n + 1}/2 = {n * (n + 1) // 2} элементов)\n\n")

        # Создаем нулевую матрицу
        matrix = [[0] * n for _ in range(n)]

        # Восстанавливаем матрицу
        index = 0
        f.write("Процесс восстановления:\n")
        for i in range(n):
            for j in range(i, n):
                matrix[i][j] = triangle_array[index]
                matrix[j][i] = triangle_array[index]
                f.write(f"  a[{i + 1}][{j + 1}] = a[{j + 1}][{i + 1}] = {triangle_array[index]}\n")
                index += 1

        f.write("\nВосстановленная симметричная матрица:\n")
        for i, row in enumerate(matrix):
            f.write(f"Строка {i + 1:2}: ")
            for num in row:
                if num.is_integer():
                    f.write(f"{int(num):4} ")
                else:
                    f.write(f"{num:6.2f} ")
            f.write("\n")

        f.write("\n")
        return matrix


def task2_process_matrix(matrix, output_file):
    """
    Задача 2: Обработка матрицы
    """
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("ЗАДАЧА 2: Обработка квадратной матрицы\n")
        f.write("=" * 60 + "\n\n")

        n = len(matrix)

        # Показываем исходную матрицу
        f.write(f"Исходная матрица {n}×{n}:\n")
        for i, row in enumerate(matrix):
            f.write(f"Строка {i + 1:2}: ")
            for num in row:
                if num.is_integer():
                    f.write(f"{int(num):6} ")
                else:
                    f.write(f"{num:8.4f} ")
            f.write("\n")

        # 1. Формируем массив диагональных элементов
        diagonal_elements = []
        f.write("\n1. Диагональные элементы:\n")
        for i in range(n):
            diag = matrix[i][i]
            diagonal_elements.append(diag)
            f.write(f"   a[{i + 1}][{i + 1}] = {diag}\n")

        f.write(f"\n   Массив диагональных элементов: {diagonal_elements}\n")

        # 2. Находим след матрицы
        trace = sum(diagonal_elements)
        f.write(f"\n2. След матрицы:\n")
        f.write(f"   Trace = {' + '.join(str(x) for x in diagonal_elements)}\n")
        f.write(f"   Trace = {trace}\n")

        # 3. Преобразуем матрицу
        f.write(f"\n3. Преобразование матрицы:\n")

        if trace == 0:
            f.write("   ВНИМАНИЕ: След матрицы равен 0!\n")
            f.write("   Деление на 0 невозможно. Преобразование не выполнено.\n")
            return matrix, diagonal_elements, trace, None

        f.write(f"   Правило: четные строки делятся на след ({trace}), нечетные без изменений\n\n")

        # Создаем копию матрицы для преобразования
        transformed_matrix = [row[:] for row in matrix]

        f.write("   Процесс преобразования:\n")
        for i in range(n):
            if (i + 1) % 2 == 0:  # четные строки
                f.write(f"\n   Строка {i + 1} (четная) - делим на {trace}:\n")
                for j in range(n):
                    original = transformed_matrix[i][j]
                    transformed_matrix[i][j] = original / trace
                    f.write(f"     a[{i + 1}][{j + 1}] = {original} / {trace} = {transformed_matrix[i][j]:.6f}\n")
            else:
                f.write(f"\n   Строка {i + 1} (нечетная) - без изменений\n")

        # 4. Показываем результат
        f.write(f"\n4. Преобразованная матрица:\n")
        for i, row in enumerate(transformed_matrix):
            f.write(f"   Строка {i + 1:2}: ")
            for num in row:
                if num.is_integer():
                    f.write(f"{int(num):10} ")
                elif abs(num) < 0.0001 or abs(num) > 10000:
                    f.write(f"{num:10.2e} ")
                else:
                    f.write(f"{num:10.6f} ")
            f.write("\n")

        return matrix, diagonal_elements, trace, transformed_matrix


def main():
    """
    Главная функция программы
    """
    # Определяем имена файлов
    student_name = "Игнатушин_ПН_ЗИТ-252"  # Замените на свои данные
    input_filename = f"{student_name}_vvod.txt"
    output_filename = f"{student_name}_vivod.txt"

    print(f"Программа обработки матриц")
    print(f"Входной файл: {input_filename}")
    print(f"Выходной файл: {output_filename}")
    print("-" * 50)

    # Проверяем существование входного файла
    if not os.path.exists(input_filename):
        print(f"ОШИБКА: Файл {input_filename} не найден!")
        print("Создайте файл с одним из следующих форматов:")
        print("\nФормат 1 (для задачи 1 - верхний треугольник):")
        print("  Строка 1: элементы верхнего треугольника через пробел")
        print("  Пример: 1 2 3 4 5 6 7 8 9 10")

        print("\nФормат 2 (для задачи 2 - квадратная матрица):")
        print("  Строка 1: размер матрицы N")
        print("  Следующие N строк: элементы строки через пробел")
        print("  Пример:")
        print("  3")
        print("  1 2 3")
        print("  4 5 6")
        print("  7 8 9")

        # Создаем пример файла
        create_example_file(input_filename)
        print(f"\nСоздан пример файла: {input_filename}")
        print("Отредактируйте его и запустите программу снова.")
        return

    # Очищаем выходной файл
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(f"Студент: {student_name}\n")
        f.write(f"Входной файл: {input_filename}\n")
        f.write("=" * 60 + "\n\n")

    # Пробуем прочитать как матрицу (задача 2)
    matrix, error = read_matrix_from_file(input_filename)

    if matrix is not None and error is None:
        print(f"✓ Успешно прочитана матрица {len(matrix)}×{len(matrix)} из файла")
        print(f"✓ Обработка матрицы...")

        # Выполняем задачу 2
        original, diagonal, trace, transformed = task2_process_matrix(matrix, output_filename)

        with open(output_filename, 'a', encoding='utf-8') as f:
            f.write("\n" + "=" * 60 + "\n")
            f.write("РЕЗЮМЕ (ЗАДАЧА 2):\n")
            f.write(f"Размер матрицы: {len(original)}×{len(original)}\n")
            f.write(f"Диагональные элементы: {diagonal}\n")
            f.write(f"След матрицы: {trace}\n")
            if transformed is not None:
                f.write("Преобразование выполнено успешно.\n")
            else:
                f.write("Преобразование не выполнено (след = 0).\n")

        print(f"✓ Результаты записаны в {output_filename}")

        # Также пробуем выполнить задачу 1 с этой же матрицей
        print(f"\nПопытка выполнить задачу 1 с восстановлением из верхнего треугольника...")

        # Создаем верхний треугольник из матрицы
        n = len(matrix)
        triangle = []
        for i in range(n):
            for j in range(i, n):
                triangle.append(matrix[i][j])

        with open(output_filename, 'a', encoding='utf-8') as f:
            f.write("\n" + "=" * 60 + "\n")
            f.write("ДОПОЛНИТЕЛЬНО: Попытка задачи 1 с текущей матрицей\n")
            f.write("=" * 60 + "\n\n")

            f.write(f"Верхний треугольник из текущей матрицы:\n")
            f.write(f"{triangle}\n\n")

        # Выполняем задачу 1
        restored_matrix = task1_restore_symmetric_matrix(triangle, output_filename)

        if restored_matrix is not None:
            print(f"✓ Матрица восстановлена из верхнего треугольника")

    else:
        # Если не удалось прочитать как матрицу, пробуем как одномерный массив (задача 1)
        print(f"Не удалось прочитать как матрицу: {error}")
        print(f"Пробуем прочитать как одномерный массив (задача 1)...")

        triangle_array, error = read_triangle_array_from_file(input_filename)

        if triangle_array is not None and error is None:
            print(f"✓ Успешно прочитан одномерный массив из {len(triangle_array)} элементов")
            print(f"✓ Восстановление симметричной матрицы...")

            # Выполняем задачу 1
            restored_matrix = task1_restore_symmetric_matrix(triangle_array, output_filename)

            if restored_matrix is not None:
                print(f"✓ Матрица восстановлена")
                print(f"✓ Выполнение задачи 2 с восстановленной матрицей...")

                # Выполняем задачу 2 с восстановленной матрицей
                original, diagonal, trace, transformed = task2_process_matrix(restored_matrix, output_filename)

                with open(output_filename, 'a', encoding='utf-8') as f:
                    f.write("\n" + "=" * 60 + "\n")
                    f.write("РЕЗЮМЕ (ЗАДАЧА 1 и 2):\n")
                    f.write(f"Элементов в массиве: {len(triangle_array)}\n")
                    f.write(f"Размер восстановленной матрицы: {len(restored_matrix)}×{len(restored_matrix)}\n")
                    f.write(f"Диагональные элементы: {diagonal}\n")
                    f.write(f"След матрицы: {trace}\n")

                print(f"✓ Результаты записаны в {output_filename}")
        else:
            print(f"✗ Ошибка при чтении файла: {error}")

            with open(output_filename, 'a', encoding='utf-8') as f:
                f.write("ОШИБКА ПРИ ЧТЕНИИ ФАЙЛА:\n")
                f.write(f"{error}\n")
                f.write("\nОжидаемые форматы файла:\n")
                f.write("1. Для задачи 1: элементы верхнего треугольника через пробел\n")
                f.write("2. Для задачи 2: первая строка - размер N, затем N строк матрицы\n")

    print(f"\n{'=' * 50}")
    print(f"Обработка завершена. Результаты в файле: {output_filename}")
    print(f"{'=' * 50}")

    # Показываем содержимое выходного файла
    try:
        with open(output_filename, 'r', encoding='utf-8') as f:
            print("\nСодержимое выходного файла:")
            print("-" * 50)
            print(f.read())
    except:
        print("Не удалось прочитать выходной файл для отображения")


def create_example_file(filename):
    """
    Создание примера входного файла
    """
    with open(filename, 'w', encoding='utf-8') as f:
        # Пример для задачи 2 (матрица 3x3)
        f.write("3\n")
        f.write("1 2 3\n")
        f.write("4 5 6\n")
        f.write("7 8 9\n")

        # Комментарии для пользователя
        f.write("\n# Этот файл содержит пример матрицы для задачи 2\n")
        f.write("# Формат:\n")
        f.write("# Строка 1: размер матрицы N\n")
        f.write("# Следующие N строк: элементы строк матрицы\n")
        f.write("\n# Для задачи 1 используйте формат:\n")
        f.write("# 1 2 3 4 5 6 7 8 9 10\n")
        f.write("# (верхний треугольник матрицы 4x4)\n")

main()