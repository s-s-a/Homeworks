from pathlib import Path

path_obj = Path("archive/2025/reports")

# parents=True — создать родительские директории, если их нет
# exist_ok=True — не вызывать ошибку, если директория уже существует
path_obj.mkdir(parents=True, exist_ok=True)
print(f"Директория '{path_obj}' успешно создана или уже существует.")
