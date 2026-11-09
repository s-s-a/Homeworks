import os

path_str = "hello.txt"
content = "Привет, мир pathlib!"

# Запись в файл
with open(path_str, "w", encoding="utf-8") as f:
    f.write(content)

# Чтение из файла
with open(path_str, "r", encoding="utf-8") as f:
    read_content = f.read()

print(read_content)
