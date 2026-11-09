import json


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


user = User("Алиса", "alice@example.com")

# Попытка сериализации
# json.dumps(user)
# -> TypeError: Object of type User is not JSON serializable


def user_serializer(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "email": obj.email}
    # Для других типов данных, которые могут вызвать ошибку,
    # вызываем стандартный обработчик
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


# вариант с default
json_string = json.dumps(user, default=user_serializer, indent=4, ensure_ascii=False)
print(json_string)

# вариант с __dict__
json_string = json.dumps(user.__dict__, indent=4, ensure_ascii=False)
print(json_string)
