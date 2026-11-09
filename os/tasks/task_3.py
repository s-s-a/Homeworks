import os
import shutil


def solve():
    """
    Задание 3: Группировка файлов по первой букве

    В папке `tasks/data_for_task_3` лежит много файлов.
    Вам нужно написать скрипт, который сгруппирует их по первой букве имени.
    1.  Для каждой буквы алфавита, с которой начинается хотя бы один файл, нужно создать папку с этой буквой (например, `A`, `B`, `C`...). Папки должны быть в верхнем регистре.
    2.  Переместить каждый файл в соответствующую ему папку.
    *   Пример: файл `apple.txt` должен быть перемещен в папку `A`, а `Bear.jpg` — в папку `B`.
    """
    data_folder = os.path.join("tasks", "data_for_task_3")

    initial_files = os.listdir(data_folder)
    item_files = [f for f in initial_files]
    for file_item in item_files:
        if not os.path.isdir(os.path.join(data_folder, file_item)):
            try:
                target_folder = os.path.join(data_folder, file_item[0].upper(), file_item)
                print(f"Файл '{file_item}' перемещен в папку '{target_folder}'")
                shutil.move(os.path.join(data_folder, file_item), target_folder)
            except Exception as e:
                print("Что-то пошло не так", {e})


if __name__ == "__main__":
    if solve():
        print("Задание 3 выполнено успешно!")
    else:
        print("Задание 3 выполнено с ошибками!")
