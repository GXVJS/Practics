import math

def calculate_s(x, y, z):
    sqrt_abs_x = math.sqrt(abs(x))
    if y <= 0:
        raise ValueError("y должен быть > 0 для ln(y)")
    ln_part = -sqrt_abs_x * math.log(y)
    # (x - y/2)
    linear_part = x - y / 2
    sin_sq_arctan = math.sin(math.atan(z)) ** 2
    # Итоговое значение
    s = ln_part * linear_part + sin_sq_arctan
    return s

def main():
    print("Вычисление выражения: s = ln(y^(-√|x|)) * (x - y/2) + sin²(arctan(z))")
    print("-" * 70)
    # Ввод данных с обработкой ошибок
    try:
        x = float(input("Введите значение x: "))
        y = float(input("Введите значение y (должно быть > 0): "))
        z = float(input("Введите значение z: "))
        # Вычисление результата
        result = calculate_s(x, y, z)
        print(f"Входные данные:")
        print(f"x = {x}")
        print(f"y = {y}")
        print(f"z = {z}")
        print(f"\nРезультат: s = {result:.6f}")
        print(f"Округлённый результат (3 знака): s = {result:.3f}")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Ошибка при вычислении: {e}")
# Пример использования с данными из задачи
if __name__ == "__main__":
    main()
    try:
        print("\nТест:")
        print("X: -15.246; Y:4.642^e-2 ; Z:21 ")
        x_test = -15.246
        y_test = 4.642e-2
        z_test = 21.0
        # Промежуточные вычисления для проверки
        sqrt_abs_x = math.sqrt(abs(x_test))
        ln_y = math.log(y_test)
        ln_part = -sqrt_abs_x * ln_y
        linear_part = x_test - y_test / 2
        sin_sq_arctan = math.sin(math.atan(z_test)) ** 2
        result = calculate_s(x_test, y_test, z_test)
        print(f"\nИтоговый результат: s = {ln_part:.6f} * {linear_part:.6f} + {sin_sq_arctan:.6f}")
        print(f"s = {result:.6f}")
    except Exception as e:
        print(f"Ошибка: {e}")