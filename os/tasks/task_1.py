import os


def solve():
    """
    Задание 1: Создание дерева директорий

    Внутри этой функции нужно написать код, который создает в папке `tasks/data_for_task_1`
    следующую структуру директорий: `media/images/icons/`. Вы должны создать все вложенные папки одной командой.
    """
    expected_path = os.path.join("tasks", "data_for_task_1", "media", "images", "icons")
    if not os.path.exists(expected_path):
        os.makedirs(expected_path, exist_ok=True)


if __name__ == "__main__":
    solve()
