# Задача 1 (Легкая): Декоратор `@debug`
# Условие:
# Напишите декоратор debug, который перед вызовом функции печатает ее имя, а также все позиционные
# и именованные аргументы, с которыми она вызывается. После вызова он должен # напечатать результат,
# который вернула функция.

# Требования:

# Декоратор должен быть простым (без параметров).
# Он должен корректно работать с любым количеством *args и **kwargs.
# Используйте @functools.wraps для сохранения метаданных.

import functools

def debug(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		result: str = ''
		result = func(*args, **kwargs)
		return f"'{func.__name__}' вернула '{result}'"

	return wrapper
# Пример использования:
@debug
def greet(name: str, greeting: str="Hello") -> str:
	return f"{greeting}, {name}!"

# Ожидаемый вывод:
# Вызывается greet('World', greeting='Hello')
# 'greet' вернула 'Hello, World!'

if __name__ == '__main__':
	print(greet("World"))
