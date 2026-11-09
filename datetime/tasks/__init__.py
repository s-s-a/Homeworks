"""
Пакет с задачами по работе с датами и временем.
"""
# Импортируем все основные функции для удобного доступа
from .task_1 import calculate_return_date
from .task_2 import calculate_age
from .task_3 import format_news_date
from .task_4 import validate_date_format
from .task_5 import analyze_timestamps

__all__ = [
    'calculate_return_date',
    'calculate_age', 
    'format_news_date',
    'validate_date_format',
    'analyze_timestamps'
]
