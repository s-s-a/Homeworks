"""
Пакет с задачами по работе со случайными значениями.
"""
# Импортируем все основные функции для удобного доступа
from .task_1 import task_1_roll_dice
from .task_2 import task_2_select_winner
from .task_3 import task_3_generate_password
from .task_4 import task_4_select_unique_prizes
from .task_5 import task_5_open_lootbox

__all__ = [
    'task_1_roll_dice',
    'task_2_select_winner',
    'task_3_generate_password',
    'task_4_select_unique_prizes',
    'task_5_open_lootbox'
]