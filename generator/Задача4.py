# Тут я использую генератор из Задача1, чтобы не создавать список чисел.
# И вообще это сразу две задачи (3 и 4) в одной.
from Задача1 import number_sequence


def gen_squares(numbers):
    """Генератор, возвращающий квадраты чисел из входной последовательности."""
    for n in numbers:
        yield n * n


if __name__ == "__main__":
    numbers = number_sequence(10)
    print(sum(gen_squares(n for n in numbers if n % 2 != 0)))
    for n in number_sequence(20) if n % 2 != 0:
        print(next(n))
