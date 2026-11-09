# Задача 5 (Сложная): Декоратор `@call_limit`
# Условие:
# Напишите фабрику декораторов call_limit, которая позволяет вызвать функцию не более указанного количества раз.
from typing import Callable


# Требования:
# Фабрика должна принимать один аргумент limit — целое число.
# При попытке вызвать функцию больше, чем limit раз, декоратор должен вызывать ValueError.
# Каждая задекорированная функция должна иметь свой собственный, независимый счетчик вызовов.

# Подсказка: Вам понадобится переменная-счетчик в области видимости декоратора (не фабрики!).
# Чтобы изменять ее из wrapper, используйте ключевое слово nonlocal.

# Пример использования:
@call_limit(limit=3)
def send_email(address):
    print(f"Отправляю письмо на {address}")

send_email("a@ex.com") # OK
send_email("b@ex.com") # OK
send_email("c@ex.com") # OK
# send_email("d@ex.com") # Вызовет ValueError

def call_limit(limit: int) -> Callable:
	def decorator(func):
		def wrapper(*args, **kwargs):