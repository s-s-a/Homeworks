import unittest
from tasks.task_4 import validate_date_format

class TestValidateDateFormat(unittest.TestCase):
    
    def test_valid_dates(self):
        """Тест корректных дат"""
        valid_dates = [
            "01/01/2025",
            "31/12/2025",
            "29/02/2024",  # високосный год
            "15/07/1990"
        ]
        
        for date in valid_dates:
            with self.subTest(date=date):
                self.assertTrue(validate_date_format(date))
    
    def test_invalid_dates(self):
        """Тест некорректных дат"""
        invalid_dates = [
            "32/01/2025",  # неверный день
            "29/02/2025",  # невисокосный год
            "31/04/2025",  # в апреле нет 31-го
            "01/13/2025",  # неверный месяц
            "01-01-2025",  # неверный формат
            "2025/01/01",  # неверный формат
            "1/1/2025",    # неверный формат (одна цифра)
            "01/01/25",    # неверный формат (короткий год)
            "invalid"      # совсем неверный формат
        ]
        
        for date in invalid_dates:
            with self.subTest(date=date):
                self.assertFalse(validate_date_format(date))
    
    def test_edge_cases(self):
        """Тест пограничных случаев"""
        # Проверим 29 февраля в високосном и невисокосном году
        self.assertTrue(validate_date_format("29/02/2024"))  # високосный
        self.assertFalse(validate_date_format("29/02/2025"))  # невисокосный

if __name__ == '__main__':
    unittest.main()
