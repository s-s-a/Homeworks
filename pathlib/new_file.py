from pathlib import Path

path_obj = Path("hello.txt")
content = "Привет, мир pathlib!"

# Запись в файл в одну строку!
path_obj.write_text(content, encoding="utf-8")

# Чтение из файла в одну строку!
read_content = path_obj.read_text(encoding="utf-8")

print(read_content)

# Для бинарных файлов существуют аналогичные методы read_bytes() и write_bytes()
if