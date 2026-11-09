# Задача: Сформировать JSON-объект, описывающий заказ в интернет-магазине, и сохранить его в файл.

import json
from datetime import datetime

# Собираем данные о заказе, используя словари и списки Python
order_data = {
    "order_id": 10543,
    "timestamp": datetime.now().isoformat(),  # Используем стандартный формат ISO 8601 для даты
    "customer": {
        "name": "Мария Смирнова",
        "email": "m.smirnova@example.com",
        "address": {
            "city": "Санкт-Петербург",
            "street": "Невский проспект",
            "house": "10",
        },
    },
    "items": [
        {
            "product_id": "prod-001",
            "product_name": "Ноутбук ProBook 15",
            "quantity": 1,
            "price": 75000.00,
        },
        {
            "product_id": "prod-025",
            "product_name": "Беспроводная мышь",
            "quantity": 1,
            "price": 1500.50,
        },
    ],
    "is_paid": True,
}

# Сохраняем сформированную структуру в файл с красивым форматированием
try:
    with open("order_10543.json", "w", encoding="utf-8") as f:
        json.dump(order_data, f, indent=4, ensure_ascii=False)

    print("Файл заказа order_10543.json успешно создан.")

except IOError as e:
    print(f"Не удалось записать файл: {e}")
