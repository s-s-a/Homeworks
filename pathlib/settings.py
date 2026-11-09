# src/settings.py
from pathlib import Path

# __file__ — это строка с путем к текущему файлу (src/settings.py)
# Path(__file__) — создаем из нее объект Path
# .resolve() — получаем полный абсолютный путь к файлу, разрешая все символические ссылки
# .parent — получаем родительскую директорию (папку 'src')
# .parent — еще раз "поднимаемся" вверх и получаем корень проекта ('my_project')
BASE_DIR = Path(__file__).resolve().parent.parent

# Теперь можно безопасно строить пути к любым ресурсам в проекте
DATA_DIR = BASE_DIR / 'data'
RAW_DATA_PATH = DATA_DIR / 'raw.csv'

print(f"Корень проекта: {BASE_DIR}")
print(f"Путь к данным: {RAW_DATA_PATH}")
print(f"Существует ли файл с данными? {RAW_DATA_PATH.exists()}")
