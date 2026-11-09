import unittest
from tasks.task_5 import task_5_open_lootbox


class TestTask5OpenLootbox(unittest.TestCase):
    def test_lootbox_with_multiple_items(self):
        """Тест лутбокса с несколькими предметами"""
        loot = {"Обычный меч": 100, "Редкий щит": 20, "Эпический шлем": 5, "Легендарный дракон": 1}
        item = task_5_open_lootbox(loot)

        self.assertIsInstance(item, str)
        self.assertIn(item, loot.keys())

    def test_lootbox_single_item(self):
        """Тест лутбокса с одним предметом"""
        loot = {"Золото": 10}
        item = task_5_open_lootbox(loot)

        self.assertEqual(item, "Золото")

    def test_lootbox_different_weights(self):
        """Тест, что предметы с бОльшим весом выпадают чаще"""
        loot = {"Частый": 1000, "Редкий": 1}
        results = []
        for _ in range(1000):
            item = task_5_open_lootbox(loot)
            results.append(item)

        frequent_count = results.count("Частый")
        rare_count = results.count("Редкий")

        # "Частый" предмет должен выпадать значительно чаще
        self.assertGreater(frequent_count, rare_count * 10)


if __name__ == "__main__":
    unittest.main()
