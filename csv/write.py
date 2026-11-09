import csv

# Данные для записи
data = [
    ['Name', 'Department', 'Salary'],
    ['Anna', 'Marketing', 75000],
    ['David', 'Engineering', 92000],
    ['Laura', 'HR', 68000]
]

with open('employees.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Записываем все данные за один раз
    writer.writerows(data)

    # Или можно записывать построчно
    # writer.writerow(['Name', 'Department', 'Salary'])
    # writer.writerow(['Anna', 'Marketing', 75000])
