import math
zadanie = int(input("Введите номер задачи"))
if zadanie == 1:
    def triangle_area(a, b):
        return 0.5 * a * b
    def rectangle_area(a, b):
        return a * b
    def quadrilateral_area(x, y, z, t):
        # Вычисляем диагональ
        diagonal = math.sqrt(x ** 2 + y ** 2)
        #площадь первого треугольника (прямоугольного)
        area1 = triangle_area(x, y)
        #площадь второго треугольника по формуле Герона
        p = (diagonal + z + t) / 2  # полупериметр
        if p > diagonal and p > z and p > t:  # проверка существования треугольника
            area2 = math.sqrt(p * (p - diagonal) * (p - z) * (p - t))
        else:
            print("Ошибка: такого четырехугольника не существует!")
            return None
        return area1 + area2
    # Ввод данных
    print("Вычисление площади четырехугольника с прямым углом между сторонами X и Y")
    X = float(input("Введите длину стороны X: "))
    Y = float(input("Введите длину стороны Y: "))
    Z = float(input("Введите длину стороны Z: "))
    T = float(input("Введите длину стороны Т: "))
    if X <= 0 or Y <= 0 or Z <= 0 or T <= 0:
        print("Ошибка: все стороны должны быть положительными числами!")
    else:
        area = quadrilateral_area(X, Y, Z, T)
        if area is not None:
            print(f"Площадь четырехугольника: {area:.4f}")

elif zadanie == 2:
    def to_octal_10_digits(number):
        # Проверка
        if number < 0:
            return "Ошибка: число должно быть неотрицательным!"
        # Преобраование в восьмеричную систему
        octal_str = oct(number)[2:]  # oct() возвращает строку вида '0o...'
        #лидирующие нули до 10 знаков
        result = octal_str.zfill(10)
        return result
    print("Перевод неотрицательного целого числа в 10-значный восьмеричный код")
    try:
        num = int(input("Введите неотрицательное целое число: "))
        # Перевод в восьмеричный код
        octal_code = to_octal_10_digits(num)
        if "Ошибка" in octal_code:
            print(octal_code)
        else:
            print(f"Десятичное число: {num}")
            print(f"Восьмеричный код (10 знаков): {octal_code}")
            print(f"Проверка (без нулей): {oct(num)[2:]}")
    except ValueError:
        print("Ошибка: введите целое число!")