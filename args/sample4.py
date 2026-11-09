import time

def timing_decorator(func):
    """Декоратор для измерения времени выполнения функции."""
    def wrapper(*args, **kwargs):
        # *args и **kwargs собирают ВСЕ аргументы, предназначенные для func
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}...")
        start_time = time.time()
        
        # Передаем собранные аргументы в оригинальную функцию
        result = func(*args, **kwargs)
        
        end_time = time.time()
        print(f"Функция {func.__name__} выполнилась за {end_time - start_time:.4f} сек.")
        return result
    return wrapper

# Применяем декоратор к функциям с разными сигнатурами
@timing_decorator
def calculate_sum(a, b, c):
    time.sleep(1)
    return a + b + c

@timing_decorator
def get_user_info(user_id, with_details=False):
    time.sleep(0.5)
    info = {'id': user_id}
    if with_details:
        info['details'] = 'Some details here'
    return info

# Вызовы
calculate_sum(10, 20, 30)
print("-" * 20)
get_user_info(101, with_details=True)