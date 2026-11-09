import unittest
from tasks.task_3 import format_news_date
from datetime import datetime


class TestFormatNewsDate(unittest.TestCase):

    def test_format_structure(self):
        """Тест структуры формата даты"""
        result: str = format_news_date()

        # Проверяем, что строка начинается с "Сегодня"
        self.assertTrue(result.startswith("Сегодня "))

        # Проверяем, что строка содержит день недели
        weekdays = [
            "Понедельник",
            "Вторник",
            "Среда",
            "Четверг",
            "Пятница",
            "Суббота",
            "Воскресенье",
        ]
        contains_weekday = any(weekday in result for weekday in weekdays)
        self.assertTrue(contains_weekday)

        # Проверяем, что строка заканчивается на " г."
        self.assertTrue(result.endswith(" г."))

    def test_contains_current_date_elements(self):
        """Тест, что строка содержит элементы текущей даты"""
        result = format_news_date()
        today = datetime.now()

        # Проверяем, что в строке есть текущий год
        self.assertIn(str(today.year), result)

        # Проверяем, что в строке есть текущий день
        self.assertIn(str(today.day), result)


if __name__ == "__main__":
    unittest.main()
