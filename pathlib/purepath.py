from pathlib import PureWindowsPath

# Этот код отлично сработает на любой ОС: Linux, macOS или Windows
win_path = PureWindowsPath("C:/Users/Admin") / "Documents" / "report.docx"

print(f"Сгенерированный путь Windows: {win_path}")  # Вывод: C:\Users\Admin\Documents\report.docx
print(f"Имя файла: {win_path.name}")
print(f"Родитель: {win_path.parent}")
