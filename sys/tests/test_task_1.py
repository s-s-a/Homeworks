import subprocess
import sys


def test_task_1_no_args():
    """Тест: запуск без аргументов - выводит пустую строку"""
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_1.py'], 
                          capture_output=True, text=True, input='', check=False)
    assert result.stdout == '\n'
    assert result.returncode == 0


def test_task_1_with_args():
    """Тест: запуск с аргументами - выводит их через пробел"""
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_1.py', 'Hello', 'world', 'from', 'Python'], 
                          capture_output=True, text=True, input='', check=False)
    assert result.stdout == 'Hello world from Python\n'
    assert result.returncode == 0


def test_task_1_single_arg():
    """Тест: запуск с одним аргументом"""
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_1.py', 'one_argument'], 
                          capture_output=True, text=True, input='', check=False)
    assert result.stdout == 'one_argument\n'
    assert result.returncode == 0