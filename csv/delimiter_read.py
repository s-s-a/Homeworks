import csv

with open('data_semicolon.csv', mode='r', newline='') as file:
    # Указываем, что разделитель — точка с запятой
    reader = csv.reader(file, delimiter=';')
    next(reader) # Пропускаем заголовок
    for row in reader:
        print(f'Товар: {row[0]}, Цена: {row[1]}')
