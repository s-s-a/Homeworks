from datetime import datetime

def format_news_date() -> str:
    """
    Функция, которая возвращает текущую дату и день недели 
    в формате "Сегодня Понедельник, 26 сентября 2025 г.".
    
    Returns:
        str: Отформатированная строка с текущей датой
    """
    # Словарь для перевода английских названий дней недели на русский
    # Для корректного вывода названий на русском может потребоваться настройка локали
    import locale
    locale.setlocale(locale.LC_ALL, ('ru_RU'))

    return datetime.now().strftime('Сегодня %A, %d %B %Y').title() + ' г.'

if __name__ == "__main__":
    print(format_news_date())
    # Пример использования функции
    
