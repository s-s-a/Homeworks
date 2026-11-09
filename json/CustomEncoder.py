from json import JSONEncoder

class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {"name": obj.name, "email": obj.email}
        # Вызываем родительский метод для обработки стандартных типов 
        # или выброса TypeError
        return super().default(obj)

json_string = json.dumps(user, cls=CustomEncoder, indent=4, ensure_ascii=False)
print(json_string)
