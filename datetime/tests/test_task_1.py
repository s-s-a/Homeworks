import unittest
from datetime import datetime, timedelta
from tasks.task_1 import calculate_return_date


class TestCalculateReturnDate(unittest.TestCase):

    def test_positive_days(self):
        """Тест с положительным количеством дней"""
        days = 14
        result = calculate_return_date(days)
        expected = datetime.now() + timedelta(days=days)

        # Проверяем, что разница не больше 1 секунды (из-за времени выполнения)
        self.assertAlmostEqual(result.timestamp(), expected.timestamp(), delta=1)

    def test_zero_days(self):
        """Тест с нулевым количеством дней"""
        days = 0
        result = calculate_return_date(days)
        expected = datetime.now()

        # Проверяем, что разница не больше 1 секунды (из-за времени выполнения)
        self.assertAlmostEqual(result.timestamp(), expected.timestamp(), delta=1)

    def test_negative_days(self):
        """Тест с отрицательным количеством дней"""
        days = -5
        result = calculate_return_date(days)
        expected = datetime.now() + timedelta(days=days)

        # Проверяем, что разница не больше 1 секунды (из-за времени выполнения)
        self.assertAlmostEqual(result.timestamp(), expected.timestamp(), delta=1)


if __name__ == "__main__":
    unittest.main()
