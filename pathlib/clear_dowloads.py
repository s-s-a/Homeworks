from pathlib import Path

# 1. Определяем директорию для работы
source_dir = Path.home() / "Downloads"

# 2. Определяем "карту" распределения: расширение -> папка
DEST_MAP = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".zip": "Archives",
    ".rar": "Archives",
}

# 3. Итерируемся по всем файлам в директории
for path in source_dir.iterdir():
    # Пропускаем директории и обрабатываем только файлы
    if path.is_dir():
        continue

    # 4. Если расширение файла есть в нашей карте
    if path.suffix in DEST_MAP:
        # Определяем папку назначения
        dest_dir_name = DEST_MAP[path.suffix]
        dest_dir = source_dir / dest_dir_name

        # 5. Создаем папку назначения, если ее нет
        dest_dir.mkdir(exist_ok=True)

        # 6. Перемещаем файл
        # Для перемещения между разными дисками лучше использовать shutil.move
        # Но для простого перемещения path.rename() идеален
        print(f"Перемещение {path.name} в {dest_dir_name}...")
        path.rename(dest_dir / path.name)
