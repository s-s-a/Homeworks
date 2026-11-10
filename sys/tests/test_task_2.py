import subprocess
import sys


def test_task_2_valid_password():
    """Тест: валидный пароль - успех"""
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_2.py', 'StrongPass123', 'StrongPass123'], 
                          capture_output=True, text=True, input='', check=False)
    assert result.stdout == 'Пароль принят.\n'
    assert result.returncode == 0


def test_task_2_wrong_number_of_args():
    """Тест: неверное количество аргументов"""
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_2.py', 'a'], 
                          capture_output=True, text=True, input='', check=False)
    assert result.stderr == 'Ошибка: Укажите пароль и его подтверждение.\n'
    assert result.returncode == 1


def test_task_2_passwords_not_match():
    """Тест: пароли не совпадают"""
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_2.py', 'Pass1', 'Pass2'], 
                          capture_output=True, text=True, input='', check=False)
    assert result.stderr == 'Ошибка: Пароли не совпадают.\n'
    assert result.returncode == 2


def test_task_2_short_password():
    """Тест: слишком короткий пароль"""
    result = subprocess.run([sys.executable, 'sys_homework/tasks/task_2.py', 'short', 'short'], 
                          capture_output=True, text=True, input='', check=False)
    assert result.stderr == 'Ошибка: Пароль слишком короткий (минимум 8 символов).\n'
    assert result.returncode == 3