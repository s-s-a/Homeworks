import subprocess
import sys
import tempfile
import os


def test_task_3_valid_file():
    """Тест: подсчет строк в существующем файле"""
    # Создаем временный файл с 3 строками
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as f:
        f.write('Line 1\n')
        f.write('Line 2\n')
        f.write('Line 3\n')
        temp_file_path = f.name
    
    # Файл должен быть закрыт до вызова subprocess
    # Контекстный менеджер автоматически закрывает файл
    
    try:
        result = subprocess.run([sys.executable, 'sys_homework/tasks/task_3.py', temp_file_path], 
                              capture_output=True, text=True)
        assert result.stdout == '3\n'
        assert result.returncode == 0
    finally:
        # Удаляем временный файл
        os.unlink(temp_file_path)


def test_task_3_no_args():
    """Тест: не передан аргумент"""
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_3.py'], 
                          capture_output=True, text=True, input='')
    assert result.stderr == 'Ошибка: Укажите путь к файлу.\n'
    assert result.returncode == 1


def test_task_3_file_not_found():
    """Тест: файл не найден"""
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_3.py', 'non_existent_file.txt'], 
                          capture_output=True, text=True, input='')
    assert result.stderr == 'Ошибка: Файл не найден.\n'
    assert result.returncode == 2