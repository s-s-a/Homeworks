from pathlib import Path

path_obj = Path("data/file.txt")

if path_obj.exists():
    if path_obj.is_file():
        print(f"Файл '{path_obj}' существует.")
    elif path_obj.is_dir():
        print(f"Директория '{path_obj}' существует.")
