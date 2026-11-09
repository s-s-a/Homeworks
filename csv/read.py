import csv

with open('users.csv', mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Пропускаем заголовок, если он не нужен
    next(csv_reader) 
    for row in csv_reader:
        # row — это список, например: ['John Smith', 'Accounting', 'November']
        print(f'{row[0]} работает в отделе {row[1]} и родился в месяце {row[2]}.')
