import random

def task_4_select_unique_prizes(prizes: list[str], count: int) -> list[str]:
    """
    Нужно выбрать несколько случайных призов из списка для награждения победителей.
    Важное условие: все выбранные призы должны быть уникальными (без повторений).

    Args:
        prizes (list[str]): Список всех возможных призов.
        count (int): Количество призов, которое нужно выбрать.

    Returns:
        list[str]: Новый список, содержащий count уникальных призов, выбранных случайным образом.
    """
    return random.sample(prizes, k=count)

if __name__ == "__main__":
    print(task_4_select_unique_prizes(["Кружка", "Футболка", "Блокнот", "Ручка", "Стикер"], 3))
