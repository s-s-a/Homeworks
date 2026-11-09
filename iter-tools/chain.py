admins = [user1, user2, ...]  # 10 000 объектов
moderators = [user3, user4, ...]  # 50 000 объектов
users = [user5, user6, ...]  # 1 000 000 объектов

# Аллокация памяти под новый список размером 1 060 000 элементов
all_people = admins + moderators + users

for person in all_people:
    process(person)

# Решение: Виртуальная склейка через chain
# Функция itertools.chain реализует паттерн проектирования «Итератор». Она принимает на вход произвольное количество итерируемых объектов и создает «виртуальную» последовательность.

import itertools  # noqa: E402

# Память не выделяется под новый список.
# Создается только легковесный объект итератора.
people_iterator = itertools.chain(admins, moderators, users)

for person in people_iterator:
    # Итератор просто переключается на следующий список,
    # когда заканчивается предыдущий.
    process(person)

# Имитация ответа от базы данных или API (список страниц)
paginated_response = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Неэффективно (создает новый список):
# flat_list = [item for page in paginated_response for item in page]

# Профессионально (ленивый итератор):
flat_iterator = itertools.chain.from_iterable(paginated_response)

for item in flat_iterator:
    print(item) # 1, 2, 3, 4...
