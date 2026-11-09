# Разбираемся со звёздочками: понятное руководство по *args и **kwargs для начинающих

## Описание

Примеры кода к статье <https://habr.com/ru/articles/958598/>

## Практические задания

## Задача 1: Обработчик списков
Условие:

Напишите функцию process_lists(*lists), которая принимает на вход произвольное количество списков. Функция должна вернуть один отсортированный по возрастанию список, содержащий все уникальные элементы из всех переданных списков.

Пример вызова:
```python
list1 = [1, 5, 3]
list2 = [3, 9, 2, 5]
list3 = [10, 1, 2]
result = process_lists(list1, list2, list3)
print(result)  # Ожидаемый вывод: [1, 2, 3, 5, 9, 10]
```
Вариант решения
```python
def process_lists(*lists):
    """
    Объединяет все элементы из переданных списков,
    оставляет только уникальные и сортирует их.
    """
    combined_set = set()
    for lst in lists:
        combined_set.update(lst)
    
    return sorted(list(combined_set))

# Пример использования
list1 = [1, 5, 3]
list2 = [3, 9, 2, 5]
list3 = [10, 1, 2]
result = process_lists(list1, list2, list3)
print(result)
```
## Задача 2: Генератор HTML-тегов
Условие:

Напишите функцию build_html_tag(tag_name, **attrs). Она должна принимать имя тега (например, 'a' или 'img') и произвольное количество именованных атрибутов (например, href="...", src="...", alt="..."). Функция должна возвращать строку, представляющую HTML-тег со всеми атрибутами.

Пример вызова:
```python
link = build_html_tag('a', href='https://example.com', target='_blank')
print(link) # Ожидаемый вывод: <a href="https://example.com" target="_blank">

image = build_html_tag('img', src='image.jpg', alt='An image')
print(image) # Ожидаемый вывод: <img src="image.jpg" alt="An image">
```
Вариант решения
```python
def build_html_tag(tag_name, **attrs):
    """
    Создает строку HTML-тега на основе имени и атрибутов.
    """
    attributes_str = ' '.join(f'{key}="{value}"' for key, value in attrs.items())
    
    # Добавляем пробел перед атрибутами, если они есть
    if attributes_str:
        attributes_str = ' ' + attributes_str
        
    return f'<{tag_name}{attributes_str}>'

# Пример использования
link = build_html_tag('a', href='https://example.com', target='_blank')
print(link)

image = build_html_tag('img', src='image.jpg', alt='An image')
print(image)

empty_div = build_html_tag('div')
print(empty_div) # Вывод: <div>
```
## Задача 3: Простой шаблонизатор
Условие:

Напишите функцию render_template(template_string, **context). Функция принимает строку-шаблон и именованные аргументы для подстановки. В шаблоне переменные для подстановки окружены двойными фигурными скобками, например {{ name }}. Функция должна заменить все вхождения {{ key }} на value из context и вернуть отформатированную строку.

Пример вызова:
```python
template = "Здравствуйте, {{ user }}! Ваша последняя активность была {{ date }}."
rendered = render_template(template, user="Иван", date="2023-10-26")
print(rendered) 
```
Ожидаемый вывод: 
```
Здравствуйте, Иван! Ваша последняя активность была 2023-10-26.
```
Вариант решения
```python
def render_template(template_string, **context):
    """
    Заменяет плейсхолдеры вида {{key}} на значения из context.
    """
    result_string = template_string
    for key, value in context.items():
        placeholder = f'{{{{ {key} }}}}' # Двойные скобки для f-строки
        result_string = result_string.replace(placeholder, str(value))
    return result_string

# Пример использования
template = "Здравствуйте, {{ user }}! Ваша последняя активность была {{ date }}."
rendered = render_template(template, user="Иван", date="2023-10-26")
print(rendered)
```
## Задача 4: Фильтрация словаря
Условие:

Напишите функцию filter_dict(source_dict, *keys_to_keep). Функция должна принимать словарь и произвольное количество строк — ключей, которые нужно оставить в словаре. Функция должна вернуть новый словарь, содержащий только те пары "ключ-значение" из исходного словаря, чьи ключи были переданы в *keys_to_keep.

Пример вызова:

```python
user_profile = {
    'username': 'johndoe',
    'email': 'john.doe@example.com',
    'password_hash': '...',
    'last_login': '2023-10-26',
    'is_active': True
}
public_profile = filter_dict(user_profile, 'username', 'last_login')
print(public_profile)
```
Ожидаемый вывод:
``` 
{'username': 'johndoe', 'last_login': '2023-10-26'}
```

Вариант решения
```python
def filter_dict(source_dict, *keys_to_keep):
    """
    Возвращает новый словарь, отфильтрованный по переданным ключам.
    """
    filtered = {}
    for key in keys_to_keep:
        if key in source_dict:
            filtered[key] = source_dict[key]
    return filtered

# Пример использования
user_profile = {
    'username': 'johndoe',
    'email': 'john.doe@example.com',
    'password_hash': '...',
    'last_login': '2023-10-26',
    'is_active': True
}
public_profile = filter_dict(user_profile, 'username', 'last_login', 'non_existent_key')
print(public_profile)
```
### Задача 5: Комбинированный отчет
Условие:

Напишите функцию generate_report(report_name, *data_rows, **report_settings).

report_name — обязательное имя отчета.

*data_rows — произвольное количество кортежей, представляющих строки данных.

**report_settings — необязательные настройки отчета, например author="Admin" или include_timestamp=True.

Функция должна распечатать отчет в следующем формате: сначала название, затем настройки (если есть), затем пронумерованные строки данных. Если настройка include_timestamp равна True, перед названием отчета нужно вывести текущую дату и время.

Пример вызова:

```python
generate_report(
    "Ежедневные продажи",
    ("Товар А", 10, 500),
    ("Товар Б", 5, 1200),
    author="Алексей",
    include_timestamp=True
)
```

Вариант решения

```python
import datetime

def generate_report(report_name, *data_rows, **report_settings):
    """
    Формирует и выводит текстовый отчет на основе переданных данных.
    """
    if report_settings.get('include_timestamp') is True:
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")

    print("--- ОТЧЕТ ---")
    print(f"Название: {report_name}")
    print("-" * 13)

    if report_settings:
        print("Настройки отчета:")
        for key, value in report_settings.items():
            print(f"  - {key}: {value}")
        print("-" * 13)

    print("Данные:")
    if not data_rows:
        print("  (пусто)")
    else:
        for i, row in enumerate(data_rows, 1):
            print(f"  {i}. {row}")
    
    print("--- КОНЕЦ ОТЧЕТА ---\n")

# Примеры использования
generate_report(
    "Ежедневные продажи",
    ("Товар А", 10, 500),
    ("Товар Б", 5, 1200),
    author="Алексей",
    include_timestamp=True
)

generate_report("Список пользователей", ("user1", "active"), ("user2", "inactive"))
```