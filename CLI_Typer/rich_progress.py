import time
from rich.progress import track
from rich import print

for step in track(range(10), description="Обработка данных..."):
    # Симулируем какую-то работу
    time.sleep(0.5)

print("[bold green]Готово![/bold green]")