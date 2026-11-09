import json

user_profile = {
    "user_id": 123,
    "username": "coder2025",
    "settings": {
        "theme": "dark",
        "notifications": True
    }
}

# Открываем файл для записи
with open("profile.json", "w", encoding="utf-8") as f:
    # Записываем словарь в файл с форматированием
    json.dump(user_profile, f, indent=4, ensure_ascii=False)

print("Файл profile.json успешно создан.")