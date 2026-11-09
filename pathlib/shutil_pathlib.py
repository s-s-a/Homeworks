import shutil
from pathlib import Path

source_dir = Path("project_backup")
destination_dir = Path("project_new")

# pathlib и shutil отлично работают вместе!
if source_dir.exists():
    shutil.rmtree(destination_dir, ignore_errors=True)  # shutil.rmtree принимает Path
    shutil.copytree(source_dir, destination_dir)  # и shutil.copytree тоже
    print("Проект успешно скопирован!")
