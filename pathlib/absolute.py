from pathlib import Path


path = Path('scripts/main.py')
print(f"Путь '{path}' абсолютный? {path.is_absolute()}") # False

# .resolve() превращает путь в абсолютный, разрешая все символические ссылки
absolute_path = path.resolve()
print(f"Абсолютный путь: {absolute_path}")
print(f"Путь '{absolute_path}' абсолютный? {absolute_path.is_absolute()}") # True
