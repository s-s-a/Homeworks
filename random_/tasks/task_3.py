import random
import string


def task_3_generate_password(length: int) -> str:
    """
    Функция для генерации случайного пароля заданной длины.
    Пароль должен состоять из ASCII-символов: строчных и прописных букв, цифр и знаков пунктуации.

    Args:
        length (int): Желаемая длина пароля (целое число).

    Returns:
        str: Строка, представляющая собой сгенерированный пароль.
    """

    # return create_new(length, characters=get_characters())
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # 2. Выбираем 'length' символов из нашего алфавита.
    #    random.choices позволяет символам повторяться, что нам и нужно.
    password_list = random.choices(all_chars, k=length)

    # 3. Соединяем список символов в одну строку
    return "".join(password_list)

if __name__ == "__main__":
    print(task_3_generate_password(10))
