"""_summary_
Запрос 3-х URL в синхронном режиме
"""

import niquests as requests
import time

# Список URL-адресов, которые мы будем запрашивать
urls = [
    'https://httpbin.org/delay/2',
    'https://httpbin.org/delay/2',
    'https://httpbin.org/delay/2',
]

def fetch_sync(url):
    """Синхронно выполняет запрос к URL."""
    print(f"Запрашиваю {url}...")
    requests.get(url)
    print(f"Запрос к {url} завершен.")

start_time = time.time()

for url in urls:
    fetch_sync(url)

end_time = time.time()

print(f"\nСинхронное выполнение заняло: {end_time - start_time:.2f} секунд.")