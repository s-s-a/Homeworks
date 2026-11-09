import msgspec
from typing import Optional

# Описываем ожидаемую структуру данных
class User(msgspec.Struct):
    name: str
    email: Optional[str] = None

# Создаем декодер для нашего типа
decoder = msgspec.json.Decoder(User)

# Декодируем и валидируем JSON
user_obj = decoder.decode(b'{"name": "Андрей", "email": "andrew@example.com"}')

print(user_obj)
# User(name='Андрей', email='andrew@example.com')

# Попытка декодировать некорректные данные вызовет ошибку
# decoder.decode(b'{"name": 123}')
# -> msgspec.ValidationError
