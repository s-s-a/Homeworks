@echo off
REM Скрипт для установки и запуска проекта в Windows

echo Установка зависимостей...
pip install -r requirements.txt

echo Запуск тестов для проверки работоспособности...
python -m pytest tests/ -v

echo Установка проекта в режиме разработки...
pip install -e .

echo Проект sys_homework инициализирован!
pause