def read_large_file(file_path):
    """
    Создает генератор для построчного чтения файла,
    не загружая весь файл в память.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

# Использование:
# Обрабатываем 10 ГБ лог-файл с минимальным потреблением памяти.
# В каждый момент времени в памяти находится только одна строка.
log_entries = read_large_file('application.log')
for entry in log_entries:
    if "ERROR" in entry:
        print(entry)