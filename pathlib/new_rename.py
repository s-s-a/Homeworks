from pathlib import Path

src = Path("main.log")
dst = Path("main.log.old")

# Метод rename можно вызвать прямо на объекте
if src.exists():
    src.rename(dst)
    print(f"Файл '{src}' переименован в '{dst}'.")
