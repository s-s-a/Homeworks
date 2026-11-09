import unittest
from tasks.task_5 import analyze_timestamps

class TestAnalyzeTimestamps(unittest.TestCase):
    
    def test_example_case(self):
        """Тест с примером из задания"""
        start_time = "2025-09-26 10:55:00"
        end_time = "2025-09-26 11:07:30"
        result = analyze_timestamps(start_time, end_time)
        
        self.assertEqual(result, "Операция заняла: 12 минут 30 секунд.")
    
    def test_same_time(self):
        """Тест с одинаковым временем"""
        start_time = "2025-09-26 10:00:00"
        end_time = "2025-09-26 10:00:00"
        result = analyze_timestamps(start_time, end_time)
        
        self.assertEqual(result, "Операция заняла: 0 минут 0 секунд.")
    
    def test_one_minute_difference(self):
        """Тест с разницей в одну минуту"""
        start_time = "2025-09-26 10:00:00"
        end_time = "2025-09-26 10:01:00"
        result = analyze_timestamps(start_time, end_time)
        
        self.assertEqual(result, "Операция заняла: 1 минут 0 секунд.")
    
    def test_one_second_difference(self):
        """Тест с разницей в одну секунду"""
        start_time = "2025-09-26 10:00:00"
        end_time = "2025-09-26 10:00:01"
        result = analyze_timestamps(start_time, end_time)
        
        self.assertEqual(result, "Операция заняла: 0 минут 1 секунд.")
    
    def test_multiple_minutes_and_seconds(self):
        """Тест с несколькими минутами и секундами"""
        start_time = "2025-09-26 10:00:00"
        end_time = "2025-09-26 10:05:30"
        result = analyze_timestamps(start_time, end_time)
        
        self.assertEqual(result, "Операция заняла: 5 минут 30 секунд.")

if __name__ == '__main__':
    unittest.main()
