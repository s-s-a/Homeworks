from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    PositiveInt,
    computed_field,
)


class UserProfile(BaseModel):
    # gt=0 - больше 0, le=120 - меньше или равно 120
    age: int = Field(gt=0, le=120, description="Возраст пользователя")

    # Готовый тип для проверки Email. Не нужно писать regex!
    email: EmailStr

    balance: PositiveInt

    @computed_field
    def status(self) -> str:
        return f"{'Basic' if self.balance < 100 else 'Pro'}"

up = UserProfile(age=35, email='sssss_aaaaa_2011@mail.ru', balance=99)

# При дампе вычисляемое поле попадает в результат автоматически!
print(up.model_dump_json())
