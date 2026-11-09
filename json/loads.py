import json

json_data = '{"name": "Анна Петрова", "city": "Москва", "skills": ["SQL", "Power BI"]}'

# Десериализуем строку в словарь Python
python_dict = json.loads(json_data)

print(python_dict)
# Вывод: {'name': 'Анна Петрова', 'city': 'Москва', 'skills': ['SQL', 'Power BI']}

# Теперь можно работать с ним как с обычным словарем
print(f"Имя: {python_dict['name']}")
# Вывод: Имя: Анна Петрова
