import unittest
from tasks.task_4 import task_4_select_unique_prizes


class TestTask4SelectUniquePrizes(unittest.TestCase):
    def test_select_unique_prizes(self):
        """Тест выбора уникальных призов"""
        prizes = ["Кружка", "Футболка", "Блокнот", "Ручка", "Стикер"]
        selected = task_4_select_unique_prizes(prizes, 3)

        self.assertEqual(len(selected), 3)
        self.assertIsInstance(selected, list)

        # Проверяем, что все выбранные призы из исходного списка
        for prize in selected:
            self.assertIn(prize, prizes)

        # Проверяем, что все призы уникальны
        self.assertEqual(len(selected), len(set(selected)))

    def test_select_all_prizes(self):
        """Тест выбора всех призов"""
        prizes = ["Кружка", "Футболка", "Блокнот"]
        selected = task_4_select_unique_prizes(prizes, 3)

        self.assertEqual(len(selected), 3)
        self.assertEqual(set(selected), set(prizes))

    def test_select_one_prize(self):
        """Тест выбора одного приза"""
        prizes = ["Книга", "Игра", "Фильм"]
        selected = task_4_select_unique_prizes(prizes, 1)

        self.assertEqual(len(selected), 1)
        self.assertIn(selected[0], prizes)

    def test_select_zero_prizes(self):
        """Тест выбора нуля призов"""
        prizes = ["Кружка", "Футболка", "Блокнот"]
        selected = task_4_select_unique_prizes(prizes, 0)

        self.assertEqual(len(selected), 0)
        self.assertEqual(selected, [])


if __name__ == "__main__":
    unittest.main()
