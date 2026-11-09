# Императивная реализация (циклы):

colors = ["Red", "Black", "White"]
sizes = ["S", "M", "L"]
materials = ["Cotton", "Polyester"]

combinations = []

# Трехуровневая вложенность
for color in colors:
    for size in sizes:
        for material in materials:
            combinations.append((color, size, material))

# Реализация через itertools.product:

# Функция product принимает произвольное количество итерируемых объектов и возвращает итератор кортежей.

import itertools  # noqa: E402

colors = ["Red", "Black", "White"]
sizes = ["S", "M", "L"]
materials = ["Cotton", "Polyester"]

# Эквивалент вложенных циклов в одну строку
sku_iterator = itertools.product(colors, sizes, materials)

for item in sku_iterator:
    print(item)
    # Output: ('Red', 'S', 'Cotton'), ('Red', 'S', 'Polyester')...

# Генерация пространства вариантов для PIN-кода длиной 4
digits = '0123456789'

# repeat=4 заменяет 4 вложенных цикла
pin_space = itertools.product(digits, repeat=4)

# Пример итерации
# ('0', '0', '0', '0')
# ('0', '0', '0', '1')
# ...
# ('9', '9', '9', '9')