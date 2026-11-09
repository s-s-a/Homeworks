from pathlib import Path

dir_path = Path("src")

# iterdir() возвращает генератор объектов Path
for item_path in dir_path.iterdir():
    # Мы сразу работаем с полноценными путями
    if item_path.is_file():
        print(f"Файл: {item_path}")
