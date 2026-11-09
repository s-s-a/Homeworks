import random
import string


def generate_password(length: int) -> str:
    """Генерирует случайный пароль заданной длины."""
    # 1. Создаем "алфавит" - строку со всеми возможными символами
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # 2. Выбираем 'length' символов из нашего алфавита.
    #    random.choices позволяет символам повторяться, что нам и нужно.
    password_list = random.choices(all_chars, k=length)

    # 3. Соединяем список символов в одну строку
    return "".join(password_list)


# Генерируем 16-значный пароль
new_password = generate_password(16)
print(f"Сгенерированный пароль: {new_password}")
