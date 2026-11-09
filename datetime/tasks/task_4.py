from datetime import datetime


def validate_date_format(date_str):
    """
    Функция, которая принимает на вход строку и проверяет,
    является ли она корректной датой в формате "ДД/ММ/ГГГГ".
    Функция должна вернуть True, если формат верный и дата существует
    (например, не "32/13/2025"), и False в противном случае.

    Args:
        date_str (str): Строка с датой в формате "ДД/ММ/ГГГГ"

    Returns:
        bool: True, если дата корректна, иначе False
    """
    try:
        dt_object_1 = datetime.strptime(date_str, "%d/%m/%Y")
        # print(f"Год из объекта: {dt_object_1.year}")
        # print(f"Строка: '{date_str}'")
        # print(date_str,f"Объект datetime: {dt_object_1.strftime('%d/%m/%Y')}")
    except:
        dt_object_1 = None
    return dt_object_1 is not None and date_str == dt_object_1.strftime("%d/%m/%Y")


if __name__ == "__main__":
    if validate_date_format("29/02/2025"):
        print("Дата корректна")
    else:
        print("Дата некорректна")
