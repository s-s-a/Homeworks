import requests

def make_api_request(method, url, *args, **kwargs):
    """
    Универсальная обертка для библиотеки requests.
    Добавляет, например, кастомный заголовок User-Agent ко всем запросам.
    """
    if 'headers' not in kwargs:
        kwargs['headers'] = {}
    kwargs['headers']['User-Agent'] = 'MyAwesomeApp/1.0'

    # requests.request - это универсальный метод, который сам принимает
    # почти любые аргументы. Мы просто передаем все "транзитом".
    return requests.request(method, url, *args, **kwargs)

# Разные вызовы с разным набором параметров
# GET-запрос с параметрами в URL
response_get = make_api_request('GET', 'https://api.github.com/events', params={'per_page': 5})

# POST-запрос с телом в формате JSON
post_data = {'title': 'New Post', 'body': 'Content'}
response_post = make_api_request('POST', 'https://jsonplaceholder.typicode.com/posts', json=post_data)

print(response_get.request.headers['User-Agent']) # Вывод: MyAwesomeApp/1.0
print(response_post.request.headers['User-Agent'])# Вывод: MyAwesomeApp/1.0