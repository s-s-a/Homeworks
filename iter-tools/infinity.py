# Ручное управление состоянием
current_id = 1000
step = 5

for data in data_stream:
    process(data, id=current_id)
    current_id += step

# Решение через itertools.count:
# Функция count(start, step) возвращает итератор, который генерирует числа бесконечно. Это идеальная пара для функции zip.

import itertools  # noqa: E402

data_stream = ["Event A", "Event B", "Event C"]

# Автоматическая генерация ID
# Аналог enumerate, но с полным контролем над стартом и шагом
id_generator = itertools.count(start=1000, step=5)

for event, event_id in zip(data_stream, id_generator):
    print(f"ID: {event_id}, Data: {event}")

# Output:
# ID: 1000, Data: Event A
# ID: 1005, Data: Event B
# ...

# Императивный подход:
# Обычно реализуется через деление по модулю (%). Это работает, но добавляет «синтаксический шум» и требует знания длины списка.

workers = ["Worker-1", "Worker-2", "Worker-3"]
tasks = range(10)

for i, task in enumerate(tasks):
    # Вычисление индекса через модуль
    worker = workers[i % len(workers)]
    assign_task(worker, task)

# Решение через itertools.cycle:
# Функция берет последовательность, запоминает её и бесконечно повторяет по кругу.

workers = ["Worker-1", "Worker-2", "Worker-3"]
tasks = range(10)

# Создаем бесконечный пул воркеров
worker_pool = itertools.cycle(workers)

for task in tasks:
    # Просто берем следующего
    current_worker = next(worker_pool)
    print(f"Задача {task} -> {current_worker}")
