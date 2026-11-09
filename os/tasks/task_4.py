
import os


def solve():
    """
    Задание 4: Сбор информации о файлах
    
    В папке `tasks/data_for_task_4` лежат файлы разных размеров. 
    Вам нужно написать код, который проанализирует эту папку и вернет из функции `solve()` словарь, где:
    *   Ключи — это строки: `'small'`, `'medium'`, `'large'`.
    *   Значения — это количество файлов, попадающих в соответствующую категорию.
    *   Критерии размера:
    *   `small`: размер файла <= 10 байт.
    *   `medium`: 10 байт < размер файла <= 100 байт.
    *   `large`: размер файла > 100 байт.
    *   Подсказка: Чтобы узнать размер файла, используйте `os.path.getsize(path_to_file)`.
    """
    data_folder = os.path.join("tasks", "data_for_task_4")

    result = {'small': 0, 'medium': 0, 'large': 0}
    initial_files = os.listdir(data_folder)
    item_files = [f for f in initial_files]
    for file_item in item_files:
        if os.path.getsize(os.path.join(data_folder, file_item)) <= 10:
            # увеличить счетчик с ключом small на единицу
            result["small"] = result["small"]+1
        elif 10 < os.path.getsize(os.path.join(data_folder, file_item)) <= 100:
            result["medium"] = result["medium"]+1
        else:
            result["large"] = result["large"]+1
    return result


if __name__ == "__main__":
    if solve():
        print("Задание 4 выполнено успешно!")
    else:
        print("Задание 4 выполнено с ошибками!")
