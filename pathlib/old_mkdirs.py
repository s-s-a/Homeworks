import os

path_str = "archive/2025/reports"

# Приходится использовать try-except или предварительную проверку
# os.makedirs() с exist_ok=True — лучший вариант в старом подходе
try:
    os.makedirs(path_str)
    print(f"Директория '{path_str}' создана.")
except FileExistsError:
    print(f"Директория '{path_str}' уже существует.")
