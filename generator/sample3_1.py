def squares_list(n):
    """
    Вычисляет квадраты чисел от 1 до n и возвращает их в виде списка.
    """
    result = []
    for i in range(1, n + 1):
        result.append(i * i)
    return result

def squares_generator(n):
    """
    Создает генератор для последовательного вычисления квадратов чисел от 1 до n.
    """
    for i in range(1, n + 1):
        yield i * i


if __name__ == '__main__':

    print(squares_list(5))
    # 1 4 9 16 25

    # Подход с материализацией
    # Потребуется память под 10 млн. чисел
    numbers_list = squares_list(10_000_000)

    # Подход с генератором
    # Память почти не расходуется, создается только объект-генератор
    squares_gen = squares_generator(10_000_000)
    # >> <generator object squares_generator at 0x...>

    for square in squares_gen:
        # Обрабатываем каждое число по отдельности
        if square > 1000:
            print(f"Первый квадрат, больший 1000: {square}")
            break # Прерываем, не вычисляя остальные миллионы значений

