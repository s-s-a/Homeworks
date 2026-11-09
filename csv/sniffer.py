import csv

# Предположим, мы не знаем формат файла unknown_data.csv
with open('unknown_data.csv', 'r', newline='') as file:
    # Берем небольшой образец данных для анализа
    sample = file.read(1024)
    file.seek(0) # Возвращаем курсор в начало файла
    
    # Sniffer определяет диалект
    dialect = csv.Sniffer().sniff(sample)
    
    # Теперь используем определенный диалект для чтения всего файла
    reader = csv.reader(file, dialect)
    for row in reader:
        print(row)
