import os

dir_path = "src"
for item_name in os.listdir(dir_path):
    # os.listdir() возвращает только имена, а не полные пути
    full_path_str = os.path.join(dir_path, item_name)
    if os.path.isfile(full_path_str):
        print(f"Файл: {full_path_str}")
