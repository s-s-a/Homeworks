import random

# --- Пример 1: Без seed ---
# При каждом запуске этого кода результат будет разным
print("Без использования seed:")
print(random.randint(1, 100))
print(random.randint(1, 100))
print("-" * 20)


# --- Пример 2: С одинаковым seed ---
# Этот блок кода всегда будет выводить одни и те же числа: 82 и 15
print("С использованием seed=42:")
random.seed(42)
print(random.randint(1, 100))  # Всегда 82
print(random.randint(1, 100))  # Всегда 15
print("-" * 20)

# Если мы сбросим seed на то же значение, последовательность начнется заново
print("Снова используем seed=42:")
random.seed(42)
print(random.randint(1, 100))  # Опять 82
print(random.randint(1, 100))  # Опять 15
