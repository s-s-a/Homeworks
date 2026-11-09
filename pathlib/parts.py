from pathlib import Path


path = Path('/home/user/project/main.py')

print(f"Родительская директория: {path.parent}")   # /home/user/project
print(f"Имя файла: {path.name}")                   # main.py
print(f"Имя без расширения: {path.stem}")          # main
print(f"Расширение: {path.suffix}")                # .py
print(f"Кортеж из частей пути: {path.parts}")      # ('/', 'home', 'user', 'project', 'main.py')
