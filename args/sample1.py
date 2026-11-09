def summator(*numbers):
    """
    Возвращает сумму всех переданных числовых аргументов.
    Внутри функции 'numbers' является кортежем.
    """
    print(f"Получен кортеж: {numbers}")  # Демонстрация типа данных
    
    total = 0
    for number in numbers:
        total += number
    return total

# Примеры вызовов функции
print(f"Сумма: {summator(1, 2, 3)}")
print("-" * 20)
print(f"Сумма: {summator(10, 20, 30, 40, 50)}")
print("-" * 20)
print(f"Сумма: {summator()}") # Функция корректно работает и без аргументов