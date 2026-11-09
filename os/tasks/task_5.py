import os


def solve():
    """
    Задание 5 (Продвинутое): Рекурсивный поиск файлов

    В папке `tasks/data_for_task_5` находится сложная структура из вложенных папок и файлов.
    Вам нужно написать код, который "пройдется" по всем папкам и подпапкам, найдет **все** файлы с расширением `.log` и вернет из функции
    `solve()` список, содержащий **полные пути** к этим файлам.
    *   Подсказка: Это идеальная задача для использования `os.walk(path)`. Этот генератор обходит все дерево директорий сверху вниз.
    Изучите, как он работает.
    """

    data_folder = os.path.join("tasks", "data_for_task_5")
    result: list[str] = []
    folder_tree = os.walk(data_folder)
    for folder in folder_tree:
        for file in folder[2]:
            if file.endswith(".log"):
                print(os.path.join(folder[0], file))
                result.append(os.path.join(folder[0], file))
        # if file.name.endswith(".log"):
            print(os.path.join(folder[0], file))
    return result


if __name__ == "__main__":
    print(solve())
