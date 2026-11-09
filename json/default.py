def user_serializer(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "email": obj.email}
    # Для других типов данных, которые могут вызвать ошибку,
    # вызываем стандартный обработчик
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

json_string = json.dumps(user, default=user_serializer, indent=4, ensure_ascii=False)
print(json_string)
