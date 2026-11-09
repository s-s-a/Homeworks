import unittest

# import pytest
from tasks.task_1 import task_1_roll_dice


class TestTask1RollDice(unittest.TestCase):
    def test_roll_dice_with_6_sides(self):
        """Тест с 6-гранным кубиком"""
        result = task_1_roll_dice(6)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)

    def test_roll_dice_with_20_sides(self):
        """Тест с 20-гранным кубиком (D&D)"""
        result = task_1_roll_dice(20)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 20)

    def test_roll_dice_with_1_side(self):
        """Тест с 1-гранным кубиком (крайний случай)"""
        result = task_1_roll_dice(1)
        self.assertEqual(result, 1)

    def test_roll_dice_with_100_sides(self):
        """Тест с 100-гранным кубиком"""
        result = task_1_roll_dice(100)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 100)


if __name__ == "__main__":
    unittest.main()
