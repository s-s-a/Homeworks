import unittest
from tasks.task_2 import task_2_select_winner


class TestTask2SelectWinner(unittest.TestCase):
    def test_select_winner_from_list(self):
        """Тест выбора победителя из списка"""
        participants = ["Анна", "Борис", "Виктор", "Дарья"]
        winner = task_2_select_winner(participants)
        self.assertIsInstance(winner, str)
        self.assertIn(winner, participants)

    def test_select_winner_single_participant(self):
        """Тест с одним участником"""
        participants = ["Алексей"]
        winner = task_2_select_winner(participants)
        self.assertEqual(winner, "Алексей")

    def test_select_winner_multiple_calls(self):
        """Тест, что каждый участник может быть выбран"""
        participants = ["Анна", "Борис", "Виктор"]
        winners = set()
        for _ in range(100):  # Делаем 100 попыток
            winner = task_2_select_winner(participants)
            self.assertIn(winner, participants)
            winners.add(winner)

        # Проверяем, что все участники могли быть выбраны
        self.assertEqual(winners, set(participants))


if __name__ == "__main__":
    unittest.main()
