def create_connection_config(host, **options):
    """
    Формирует словарь конфигурации.
    'host' - обязательный позиционный аргумент.
    'options' - словарь, содержащий все остальные именованные аргументы.
    """
    config = {'host': host}
    print(f"Получен словарь опций: {options}")  # Демонстрация типа данных

    # Метод update() словаря идеально подходит для слияния
    config.update(options)
    return config

# Пример 1: передача базовых параметров
config1 = create_connection_config("localhost", user="admin", port=5432)
print(f"Итоговая конфигурация 1: {config1}\n")

# Пример 2: передача расширенного набора параметров
config2 = create_connection_config(
    "db.example.com",
    user="readonly_user",
    password="secure_password",
    timeout=30,
    ssl_mode="require"
)
print(f"Итоговая конфигурация 2: {config2}")