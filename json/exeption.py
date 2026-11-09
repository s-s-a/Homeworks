import json

invalid_json = f'{"name": "Боб", "age": 40,}' # Лишняя запятая в конце

try:
    data = json.loads(invalid_json)
    print("JSON успешно разобран:", data)
except json.JSONDecodeError as e:
    print("Ошибка декодирования JSON!")
    print(f"Сообщение об ошибке: {e.msg}")
    print(f"Строка: {e.lineno}, колонка: {e.colno}")
