import os

def solve():
    """
    Задание 2: Очистка от временных файлов
    
    В папке `tasks/data_for_task_2` находится беспорядок из разных файлов. 
    Вам нужно написать код, который найдет и **удалит** все файлы, заканчивающиеся на `.tmp`. 
    Другие файлы должны остаться нетронутыми.
    """
    
    data_folder = os.path.join('tasks', 'data_for_task_2')
    
    # Проверяем, что в папке есть .tmp файлы до выполнения задания
    initial_files = os.listdir(data_folder)
    tmp_files = [f for f in initial_files if f.endswith('.tmp')]
    for file_item in tmp_files:
        if file_item.endswith('.tmp'):
            os.remove(os.path.join(data_folder, file_item))
        else:
            print(f"Файл {file_item} не является .tmp файлом и не будет удален.")


if __name__ == "__main__":
    solve()
    print("Задание 2 выполнено успешно!")