import json

# Открываем файл для чтения
with open("profile.json", "r", encoding="utf-8") as f:
    # Загружаем данные из файла в переменную
    data = json.load(f)

print(data)
# Вывод: {'user_id': 123, 'username': 'coder2025', 'settings': {'theme': 'dark', 'notifications': True}}

print(f"Тема оформления: {data['settings']['theme']}")
# Вывод: Тема оформления: dark