import random


def estimate_pi(num_points: int) -> float:
    """Оценивает число Пи методом Монте-Карло."""
    points_in_circle = 0

    for _ in range(num_points):
        # Генерируем случайную точку (x, y) в квадрате 1x1
        x = random.random()
        y = random.random()

        # Проверяем, находится ли точка внутри круга с радиусом 1
        # по формуле x² + y² <= r² (где r=1)
        if x**2 + y**2 <= 1:
            points_in_circle += 1

    # Вычисляем Пи по формуле
    return 4 * points_in_circle / num_points


# Чем больше точек, тем точнее результат
pi_estimate = estimate_pi(1_000_000)
print(f"Примерная оценка числа Пи: {pi_estimate}")
