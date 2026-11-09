import os

old_name = "main.log"
new_name = "main.log.old"

# Убедимся, что файл существует
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"Файл '{old_name}' переименован в '{new_name}'.")
