from pathlib import Path

# Директория для поиска (например, домашняя)
search_dir = Path.home()

# 1. Используем rglob для рекурсивного поиска всех файлов
# 2. Фильтруем, оставляя только файлы (на случай, если попадется ссылка на директорию)
# 3. Создаем список кортежей (размер_файла, путь_к_файлу)
all_files = [(p.stat().st_size, p) for p in search_dir.rglob("*") if p.is_file()]

# 4. Сортируем список по убыванию размера и берем первые 10
all_files.sort(key=lambda x: x[0], reverse=True)

print("Топ-10 самых больших файлов:")
for size, path in all_files[:10]:
    # Приводим размер к мегабайтам для читаемости
    print(f"  {path.name:<40} | {size / 1024 / 1024:.2f} MB")
