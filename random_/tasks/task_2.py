import random

def task_2_select_winner(participants: list[str]) -> str:
    """
    У вас есть список участников лотереи. Напишите функцию, которая выбирает и возвращает имя одного случайного победителя.

    Args:
        participants (list[str]): Список строк, где каждая строка — это имя участника.

    Returns:
        str: Строка с именем одного случайно выбранного участника.
    """
    return random.choice(participants)

if __name__ == "__main__":
    print(random.choice(["Анна", "Борис", "Виктор", "Дарья"]))