def simple_generator():
    yield 1
    yield 2

# Создание объекта-генератора. Код внутри функции еще не выполняется.
gen = simple_generator()

# Цикл for последовательно извлекает все значения из генератора
for value in gen:
    print(value)

# Вывод:
# 1
# 2

gen = simple_generator() # Создаем новый экземпляр

print(next(gen)) # Запускает выполнение до первого yield, возвращает 1
# Вывод: 1

print(next(gen)) # Возобновляет выполнение до второго yield, возвращает 2
# Вывод: 2

gen = simple_generator()# Создаем новый экземпляр

# Первый проход - все работает
print("Первый проход:")
for value in gen:
    print(value)

# Второй проход - генератор уже пуст
print("\nВторой проход:")
for value in gen:
    print(value) # Этот код никогда не выполнится

# Вывод:
# Первый проход:
# 1
# 2
#
# Второй проход: