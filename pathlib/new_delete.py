from pathlib import Path

file_to_del = Path("temp.tmp")
dir_to_del = Path("temp_dir")

# .unlink() для файлов (и символических ссылок)
if file_to_del.exists():
    file_to_del.unlink()

# .rmdir() для пустых директорий
if dir_to_del.exists():
    dir_to_del.rmdir()

# для рекурсивного удаления непустой директории по-прежнему стоит использовать shutil.rmtree(),
# который, впрочем, прекрасно принимает в качестве аргумента объект Path
