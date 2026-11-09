from json import JSONEncoder
import json


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


user = User("Алиса", "alice@example.com")


class CustomEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "email": o.email}
        # Вызываем родительский метод для обработки стандартных типов
        # или выброса TypeError
        return super().default(o)


json_string = json.dumps(user, cls=CustomEncoder, indent=4, ensure_ascii=False)
print(json_string)
