import unittest
import string
from tasks.task_3 import task_3_generate_password


class TestTask3GeneratePassword(unittest.TestCase):
    def test_password_length(self):
        """Тест длины пароля"""
        length = 12
        password = task_3_generate_password(length)
        self.assertEqual(len(password), length)

    def test_password_length_zero(self):
        """Тест с длиной 0"""
        password = task_3_generate_password(0)
        self.assertEqual(len(password), 0)

    def test_password_contains_valid_chars(self):
        """Тест, что пароль содержит только допустимые символы"""
        length = 50
        password = task_3_generate_password(length)

        valid_chars = set(string.ascii_letters + string.digits + string.punctuation)
        password_chars = set(password)

        # Проверяем, что все символы в пароле допустимы
        self.assertTrue(password_chars.issubset(valid_chars))

    def test_password_different_each_time(self):
        """Тест, что пароли разные при разных вызовах"""
        passwords = set()
        for _ in range(100):
            password = task_3_generate_password(10)
            passwords.add(password)

        # Хотя бы некоторые должны отличаться (с высокой вероятностью)
        self.assertGreater(len(passwords), 50)


if __name__ == "__main__":
    unittest.main()
