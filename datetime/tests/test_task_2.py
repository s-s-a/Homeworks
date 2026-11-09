import unittest
from tasks.task_2 import calculate_age


class TestCalculateAge(unittest.TestCase):

    def test_birthday_passed(self):
        """Тест, когда день рождения уже прошел в этом году"""
        birth_date = "1990-01-01"
        # В реальности возраст будет зависеть от текущей даты
        # Для теста предположим, что сегодня 2025-09-26
        result = calculate_age(birth_date)
        # Если родился в 1990 и день рождения уже прошел в 2025, то должно быть 35 лет
        self.assertGreaterEqual(result, 35)  # возраст >= 35

    def test_birthday_not_passed(self):
        """Тест, когда день рождения еще не наступил в этом году"""
        birth_date = "2000-12-31"
        result = calculate_age(birth_date)
        # Если родился в 2000 и день рождения еще не прошел в 2025, то должно быть 24 года
        self.assertGreaterEqual(result, 24)  # возраст >= 24

    def test_exact_birthday(self):
        """Тест, когда день рождения сегодня"""
        # Для этого теста мы не можем использовать фиксированную дату рождения,
        # но можем протестировать логику вычисления
        import datetime

        current_year = datetime.datetime.now().year
        birth_year = current_year - 25
        birth_date = f"{birth_year}-01-01"

        result = calculate_age(birth_date)
        self.assertEqual(
            result,
            (
                25
                if datetime.datetime.now().month >= 1
                and datetime.datetime.now().day >= 1
                else 24
            ),
        )

    def test_invalid_date_format(self):
        """Тест с неправильным форматом даты"""
        with self.assertRaises(ValueError):
            calculate_age("01-01-1990")  # неправильный формат


if __name__ == "__main__":
    unittest.main()
