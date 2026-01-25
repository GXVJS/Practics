print("Введите номер задачи ")
z = int(input())
if z == 1:
    arr = list(map(int, input("Введите числа пробел").split()))

    sum_even = 0
    product_odd = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            sum_even += arr[i]
        else:
            product_odd += arr[i]
            has_odd = True
    if not has_odd:
        product_odd = 0

    print("Сумма элементов с чётными номерами: ",sum_even)
    print("Произведение элементов с нечётными номерами:  ",product_odd)
elif z == 2:
    arr = list(map(int, input("Введите числа через пробел: ").split()))
    if arr:
        min_index = 0
        max_index = 0

        for i in range(1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i
            if arr[i] > arr[max_index]:
                max_index = i
        arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

        print("Массив после перестановки:", arr)
    else:
        print("Массив пуст!")