import glob
import os

# Нужно вручную конструировать путь для поиска
search_pattern = os.path.join("src", "**", "*.py")

# recursive=True необходимо для работы '**'
py_files = glob.glob(search_pattern, recursive=True)

for file_path_str in py_files:
    # Мы получаем строки, которые для дальнейшей работы нужно снова превращать в объекты
    print(file_path_str)
