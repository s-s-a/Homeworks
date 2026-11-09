from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, FilePath, HttpUrl, computed_field


class UserProfile(BaseModel):
    # gt=0 - больше 0, le=120 - меньше или равно 120
    age: int = Field(gt=0, le=120, description="Возраст пользователя")

    # Готовый тип для ��роверки Email. Не нужно писать regex!
    email: EmailStr

    # Проверка, что строка является валидным URL
    website: HttpUrl

    # папка загрузок
    load_path: FilePath


# Попытка создать некорректный профиль
# UserProfile(age=150, email="not-an-email", website="http://broken", load_path='..')
# Вызовет ValidationError с описанием всех трех ошибок сразу.

#=======================================================================================================

class Event(BaseModel):
    title: str
    timestamp: datetime

event = Event(title="Запуск сервера", timestamp=datetime.now())

# В dataclasses здесь была бы ошибка или танцы с бубном
json_data = event.model_dump_json()

print(json_data)
# {"title":"Запуск сервера","timestamp":"2025-11-26T10:00:00.123456"}

#=======================================================================================================


class Employee(BaseModel):
    first_name: str
    last_name: str

    @computed_field
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

emp = Employee(first_name="Иван", last_name="Иванов")

# При дампе вычисляемое поле попадает в результат автоматически!
print(emp.model_dump_json())
# {"first_name":"Иван", "last_name":"Иванов", "full_name":"Иван Иванов"}