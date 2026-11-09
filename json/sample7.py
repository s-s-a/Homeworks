import json


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<User {self.name} ({self.email})>"


def user_decoder(dct):
    # Проверяем, похож ли словарь на нашего пользователя (например, по ключам)
    if "name" in dct and "email" in dct:
        return User(dct["name"], dct["email"])
    return dct


json_string = '{"name": "Алиса", "email": "alice@example.com"}'

# Десериализуем строку с использованием object_hook
user_obj = json.loads(json_string, object_hook=user_decoder)

print(user_obj)
print(type(user_obj))
