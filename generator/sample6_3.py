# Шаг 1: Генератор-источник (как в примере 6.1)
def read_log(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line

# Шаг 2: Генератор-фильтр
def filter_lines(sequence, substring):
    for line in sequence:
        if substring in line:
            yield line

# Шаг 3: Генератор-преобразователь
def extract_ip(sequence):
    for line in sequence:
        ip = line.split()[0]
        yield ip

# Сборка и запуск конвейера:
log_lines = read_log('access.log')
post_requests = filter_lines(log_lines, 'POST /api/v1/auth')
ip_addresses = extract_ip(post_requests)

# На этом этапе еще не было прочитано ни одной строки!
# Обработка запускается только циклом for.
unique_ips = set(ip_addresses)
print(f"Найдено уникальных IP-адресов: {len(unique_ips)}")