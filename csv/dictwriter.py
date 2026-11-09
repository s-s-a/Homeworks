import csv

# Данные в виде списка словарей
data = [
    {'Name': 'Anna', 'Department': 'Marketing', 'Salary': 75000},
    {'Name': 'David', 'Department': 'Engineering', 'Salary': 92000},
    {'Name': 'Laura', 'Department': 'HR', 'Salary': 68000}
]

# Список с именами полей
fieldnames = ['Name', 'Department', 'Salary']

with open('employees_dict.csv', mode='w', newline='') as csv_file:
    # fieldnames — обязательный параметр
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Записываем первую строку с заголовками
    writer.writeheader()
    
    # Записываем все данные
    writer.writerows(data)
