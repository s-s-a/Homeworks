# Поиск пар (Сочетания)

# Императивный подход (Вложенные циклы):
# Чтобы избежать дубликатов (матч "Команда А vs Команда Б" и "Команда Б vs Команда А" — это одна игра) и матчей с самими собой, во внутреннем цикле приходится манипулировать индексами (j = i + 1).

teams = ['Team A', 'Team B', 'Team C', 'Team D']
matches = []

for i in range(len(teams)):
    # Начинаем с i + 1, чтобы не повторяться
    for j in range(i + 1, len(teams)):
        matches.append((teams[i], teams[j]))

# Результат: [('Team A', 'Team B'), ('Team A', 'Team C')...]

# Решение через itertools.combinations:
# Функция принимает итерируемый объект и длину выходного кортежа r.

import itertools  # noqa: E402

teams = ['Team A', 'Team B', 'Team C', 'Team D']

# r=2 означает, что мы ищем пары
match_iterator = itertools.combinations(teams, 2)

for match in match_iterator:
    print(match)
    # Гарантированно уникальные пары без учета порядка

# Варианты размещения (Перестановки)

# Решение через itertools.permutations:

participants = ['Ivanov', 'Petrov', 'Sidorov']

# Генерируем все возможные варианты распределения 3 мест
# Если второй аргумент не указан, он равен длине списка
awards_variants = itertools.permutations(participants, 3)

print(list(awards_variants))
# [
#   ('Ivanov', 'Petrov', 'Sidorov'), 
#   ('Ivanov', 'Sidorov', 'Petrov'),
#   ('Petrov', 'Ivanov', 'Sidorov'),
#   ...
# ]

