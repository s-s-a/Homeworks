from pathlib import Path

project_dir = Path("src")

# rglob возвращает генератор, что экономит память
py_files_generator = project_dir.rglob("*.py")

for path_obj in py_files_generator:
    # Мы сразу получаем Path объекты, готовые к работе!
    print(f"Найден файл: {path_obj}, размер: {path_obj.stat().st_size} байт")
