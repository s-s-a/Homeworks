from pathlib import Path


# Создаем путь к файлу
config_path = Path('settings/production/database.ini')

# Получаем специальные пути
current_dir = Path.cwd()  # Current Working Directory (текущая рабочая директория)
home_dir = Path.home()    # Домашняя директория пользователя

print(f"Путь к конфигу: {config_path}")
print(f"Текущая директория: {current_dir}")
print(f"Домашняя директория: {home_dir}")
