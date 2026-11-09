# Задача 4 (Средняя+): Декоратор `@to_json`
# Условие:
# Напишите декоратор @to_json, который преобразует результат выполнения функции
# (предполагается, что это словарь) в строку формата JSON.

# Требования:

# Декоратор должен быть простым (без параметров).
# Вам понадобится import json и функция json.dumps().
# Декоратор должен перехватывать результат работы исходной функции, преобразовывать его и возвращать уже строку.

# Пример использования:
import json

@to_json
def get_user_data(user_id):
    return {"id": user_id, "name": "John Doe", "permissions": ["read", "write"]}

json_string = get_user_data(123)
print(json_string)
# Выведет: {"id": 123, "name": "John Doe", "permissions": ["read", "write"]}
print(type(json_string)) # Выведет: <class 'str'>
