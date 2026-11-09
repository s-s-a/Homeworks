from random import randint

def task_1_roll_dice(sides: int) -> int:
    """
    Функция, которая имитирует бросок одного игрального кубика с заданным количеством граней.

    Args:
        sides (int): Количество граней у кубика (целое число). Например, для стандартного кубика это будет 6.

    Returns:
        int: Случайное целое число в диапазоне от 1 до sides включительно.
    """
    return randint(1, sides)


# @pytest.mark.parametrize("sides", [6, 20, 1, 100])
# def test_task_1_roll_dice(sides):
#     result = task_1_roll_dice(sides)
#     assert isinstance(result, int)
#     assert 1 <= result <= 6


if __name__ == "__main__":
    print(task_1_roll_dice(6))
