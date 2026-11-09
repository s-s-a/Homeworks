# site_checker_async.py
import asyncio
from pathlib import Path
import typer
import httpx
import csv
from rich.console import Console
from rich.table import Table
from typing import Optional

console = Console()

DEFAULT_URLS = [
    "https://httpbin.org/get",           # 200
    "https://httpbin.org/redirect/1",    # 302
    "https://httpbin.org/status/404",    # 404
    "https://httpbin.org/status/500",    # 500
]

def get_status_emoji(status_code: int) -> str:
    """Возвращает эмодзи в зависимости от статус-кода."""
    status_emoji_map = {
        2: "✅ OK",
        3: "➡️ REDIRECT",
        4: "❌ CLIENT ERROR",
        5: "🔥 SERVER ERROR",
    }
    return status_emoji_map.get(status_code // 100, "❓ UNKNOWN")


async def check_url(client: httpx.AsyncClient, url: str) -> dict:
    """
    Асинхронно проверяет один URL и возвращает результат.
    """
    try:
        response = await client.get(url)
        status_code = response.status_code
        status_text = get_status_emoji(status_code)

        row_style = ""
        if 300 <= status_code < 400:
            row_style = "yellow"
        elif status_code >= 400:
            row_style = "red"

        return {
            "url": url,
            "status_code": str(status_code),
            "status_text": status_text,
            "style": row_style,
        }
    except httpx.RequestError as e:
        return {
            "url": url,
            "status_code": "N/A",
            "status_text": f"💥 ERROR: {e.__class__.__name__}",
            "style": "bold red",
        }


async def main_async(
    urls: list[str], timeout: float, output_file: Optional[str]
) -> Table:
    """
    Асинхронно проверяет список URL, выводит таблицу и при необходимости сохраняет результат в CSV.
    """
    table = Table(title="Результаты проверки сайтов")
    table.add_column("URL", style="cyan", no_wrap=True)
    table.add_column("Статус код", justify="center")
    table.add_column("Статус", justify="left")

    csv_data = []

    async with httpx.AsyncClient(follow_redirects=True, timeout=timeout) as client:
        tasks = [check_url(client, url) for url in urls]
        results = await asyncio.gather(*tasks)

    for result in results:
        table.add_row(
            result["url"],
            result["status_code"],
            result["status_text"],
            style=result["style"],
        )
        csv_data.append(
            {
                "URL": result["url"],
                "Status Code": result["status_code"],
                "Status": result["status_text"],
            }
        )

    if output_file:
        try:
            with open(output_file, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["URL", "Status Code", "Status"])
                writer.writeheader()
                writer.writerows(csv_data)
            console.print(f"\n✅ Результат сохранён в [bold green]{output_file}[/bold green]")
        except Exception as e:
            console.print(f"\n❌ Не удалось сохранить файл: [bold red]{e}[/bold red]")

    return table


def load_urls_from_file(file_path: str) -> list[str]:
    """Читает URL из файла с помощью Path.read_text(), по одному на строку, пропуская пустые и комментарии."""
    try:
        file = Path(file_path)
        content = file.read_text(encoding="utf-8")
        urls = []
        for line in content.splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                urls.append(line)
        if not urls:
            raise ValueError("Файл пуст или не содержит допустимых URL")
        return urls
    except FileNotFoundError:
        console.print(f"[bold red]❌ Ошибка: файл '{file_path}' не найден.[/bold red]")
        raise typer.Exit(code=1)
    except PermissionError:
        console.print(f"[bold red]❌ Ошибка: нет доступа к файлу '{file_path}'.[/bold red]")
        raise typer.Exit(code=1)
    except Exception as e:
        console.print(f"[bold red]❌ Ошибка чтения файла: {e}[/bold red]")
        raise typer.Exit(code=1)


def main(
    urls: list[str] = typer.Argument(DEFAULT_URLS, help="Список URL для проверки."),
    input_file: Optional[str] = typer.Option(None, "--input-file", "-i", help="Файл с URL (по одному на строку)."),
    timeout: int = typer.Option(5, "--timeout", "-t", help="Таймаут для каждого запроса в секундах."),
    output_file: Optional[str] = typer.Option(None, "--output", "-o", help="Сохранить результат в CSV файл."),
):
    """
    Проверяет доступность сайтов и выводит результат в виде таблицы (асинхронно).
    Поддерживает ввод из файла и вывод в CSV.
    """
    # Проверка конфликта: нельзя использовать и аргументы, и файл
    if input_file and urls != DEFAULT_URLS:
        console.print(
            "[bold red]❌ Ошибка: нельзя одновременно указывать URL в аргументах и --input-file.[/bold red]"
        )
        console.print("Используйте либо аргументы, либо файл, но не оба варианта.")
        raise typer.Exit(code=1)

    # Определяем, откуда брать URL
    if input_file:
        console.print(f"[cyan]📖 Загрузка URL из файла: {input_file}[/cyan]")
        urls = load_urls_from_file(input_file)

    # Запуск основной логики
    table = asyncio.run(main_async(urls, float(timeout), output_file))
    console.print(table)


if __name__ == "__main__":
    typer.run(main)
