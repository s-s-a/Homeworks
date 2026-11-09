# Императивный подход (Словарь списков)
# Традиционное решение на Python подразумевает создание промежуточного словаря, где ключом является признак группировки, а значением — список объектов.

transactions = [
    {"date": "2023-10-01", "amount": 100, "id": 1},
    {"date": "2023-10-02", "amount": 200, "id": 2},
    {"date": "2023-10-01", "amount": 150, "id": 3},
]

grouped_data = {}

for tx in transactions:
    date = tx["date"]
    if date not in grouped_data:
        grouped_data[date] = []
    grouped_data[date].append(tx)

# Результат: словарь с двумя ключами и списками транзакций

# Важное правило: Входные данные для groupby обязательно должны быть отсортированы по ключу группировки.

# Корректная реализация:

import itertools  # noqa: E402
from operator import itemgetter  # noqa: E402

transactions = [
    {"date": "2023-10-01", "amount": 100, "id": 1},
    {"date": "2023-10-02", "amount": 200, "id": 2},
    {"date": "2023-10-01", "amount": 150, "id": 3},
]

# 1. Обязательная сортировка данных
# Используем itemgetter для извлечения ключа (быстрее, чем lambda)
key_func = itemgetter("date")
transactions.sort(key=key_func)

# 2. Группировка
# groupby возвращает итератор, поэтому используем цикл
for date, group_iterator in itertools.groupby(transactions, key=key_func):

    # group_iterator — это тоже итератор!
    # Чтобы работать с данными, их часто нужно превратить в список
    # или агрегировать (например, посчитать сумму)

    total_amount = sum(item["amount"] for item in group_iterator)
    print(f"Дата: {date}, Сумма: {total_amount}")

# Output:
# Дата: 2023-10-01, Сумма: 250
# Дата: 2023-10-02, Сумма: 200

raw_data = "AAAABBBCCDAA"
compressed = []

for char, group in itertools.groupby(raw_data):
    # group преобразуем в список, чтобы узнать его длину
    count = len(list(group))
    compressed.append((char, count))

print(compressed)
# [('A', 4), ('B', 3), ('C', 2), ('D', 1), ('A', 2)]
