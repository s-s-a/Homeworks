import requests
import json

# Имя пользователя, чьи репозитории мы хотим получить
username = "user123"
# Формируем URL для запроса к API GitHub
url = f"https://api.github.com/users/{username}/repos"

try:
    # Отправляем GET-запрос
    response = requests.get(url)
    # Проверяем, что запрос успешен (статус код 200)
    response.raise_for_status()

    # Десериализуем полученный JSON-ответ. 
    # Библиотека requests имеет встроенный метод .json(), который делает это за нас.
    # Это эквивалентно json.loads(response.text)
    repos_data = response.json()

    print(f"Публичные репозитории пользователя {username}:")
    
    # Перебираем список репозиториев (который теперь является списком словарей Python)
    for repo in repos_data:
        # Извлекаем нужные данные по ключам
        repo_name = repo["name"]
        repo_url = repo["html_url"]
        print(f"- {repo_name}: {repo_url}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при выполнении запроса: {e}")
except json.JSONDecodeError:
    print("Ошибка декодирования JSON. Получен невалидный ответ от сервера.")
