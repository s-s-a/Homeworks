import subprocess
import sys


def test_task_5_pattern_found():
    """Тест: строки с паттерном находятся"""
    input_data = "[INFO] User logged in\n[DEBUG] Checking cache\n[ERROR] Failed to connect to DB\n[INFO] User logged out\n"
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_5.py', '[INFO]'], 
                          capture_output=True, text=True, input=input_data)
    
    expected_output = "[INFO] User logged in\n[INFO] User logged out\n"
    assert result.stdout == expected_output
    assert result.returncode == 0


def test_task_5_pattern_not_found():
    """Тест: паттерн не найден - ничего не выводится"""
    input_data = "[INFO] User logged in\n[DEBUG] Checking cache\n[ERROR] Failed to connect to DB\n"
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_5.py', 'WARNING'], 
                          capture_output=True, text=True, input=input_data)
    
    assert result.stdout == ''
    assert result.returncode == 0


def test_task_5_no_args():
    """Тест: не передан аргумент"""
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_5.py'], 
                          capture_output=True, text=True, input='')
    
    assert result.stderr == 'Ошибка: Укажите паттерн для поиска.\n'
    assert result.returncode == 1


def test_task_5_single_match():
    """Тест: одна строка содержит паттерн"""
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_5.py', 'DB'], 
                          capture_output=True, text=True, input='[ERROR] Failed to connect to DB\n[INFO] System up')
    
    assert result.stdout == '[ERROR] Failed to connect to DB\n'
    assert result.returncode == 0