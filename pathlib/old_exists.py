import os

path_str = 'data/file.txt'

if os.path.exists(path_str):
    if os.path.isfile(path_str):
        print(f"Файл '{path_str}' существует.")
    elif os.path.isdir(path_str):
        print(f"Директория '{path_str}' существует.")
