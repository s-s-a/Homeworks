from rich import print
from rich.table import Table

# 1. Создаем объект таблицы
table = Table(title="Список моих любимых фреймворков")

# 2. Добавляем колонки
table.add_column("Название", justify="left", style="cyan", no_wrap=True)
table.add_column("Язык", style="magenta")
table.add_column("Для чего", justify="right", style="green")

# 3. Наполняем данными
table.add_row("FastAPI", "Python", "Веб-API")
table.add_row("React", "JavaScript", "Фронтенд")
table.add_row("Typer", "Python", "CLI-приложения")

# 4. Выводим таблицу в консоль
print(table)