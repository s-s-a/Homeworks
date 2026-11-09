import json

# Создаем словарь Python
user_data = {
    "name": "Иван Иванов",
    "age": 30,
    "is_active": True,
    "courses": ["Python", "Git"],
    "passport": None
}

# Сериализуем в JSON-строку
json_string = json.dumps(user_data)

print(json_string)
# Вывод: {"name": "\u0418\u0432\u0430\u043d \u0418\u0432\u0430\u043d\u043e\u0432", "age": 30, "is_active": true, "courses": ["Python", "Git"], "passport": null}

# Используем ensure_ascii=False для корректного отображения кириллицы
json_formatted_string = json.dumps(user_data, indent=4, sort_keys=True, ensure_ascii=False)

print(json_formatted_string)