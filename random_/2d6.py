import random


def roll_dice() -> int:
    """Имитирует бросок двух шестигранных кубиков и возвращает сумму."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"Бросок: {die1} + {die2} = {total}")
    return total


# Совершаем бросок
roll_result = roll_dice()
