import csv
from pathlib import Path

# Создаем путь к файлу, который будет работать на любой ОС
data_folder = Path('data') / 'reports'
file_path = data_folder / 'report.csv'

# Убедимся, что директории существуют
data_folder.mkdir(parents=True, exist_ok=True)

with open(file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'value'])
    writer.writerow(['1', '100'])
