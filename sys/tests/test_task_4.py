import subprocess
import sys


def test_task_4_input():
    """Тест: чтение из stdin с нумерацией строк"""
    input_data = "Молоко\nХлеб\nМасло\n"
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_4.py'], 
                          capture_output=True, text=True, input=input_data, check=False)
    
    expected_output = "1: Молоко\n2: Хлеб\n3: Масло\n"
    assert result.stdout == expected_output
    assert result.returncode == 0


def test_task_4_empty_input():
    """Тест: пустой ввод"""
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_4.py'], 
                          capture_output=True, text=True, input='', check=False)
    
    assert result.stdout == ''
    assert result.returncode == 0


def test_task_4_single_line():
    """Тест: одна строка во вводе"""
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_4.py'], 
                          capture_output=True, text=True, input='Одна строка', check=False)
    
    assert result.stdout == '1: Одна строка'
    assert result.returncode == 0