import csv

with open('users.csv', mode='r', newline='') as csv_file:
    # Создаем объект DictReader
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        # Теперь row — это словарь
        # Например: {'name': 'John Smith', 'department': 'Accounting', 'birth_month': 'November'}
        print(f"{row['name']} работает в отделе {row['department']}.")
