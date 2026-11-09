data_to_write = [
    ['ID', 'Name', 'Status'],
    [101, 'Project "Alpha"', 'In Progress'],
    [102, 'Project "Beta"', 'Completed']
]

with open('projects.tsv', mode='w', newline='') as file:
    # Указываем разделитель-табуляцию и режим полного квотирования
    writer = csv.writer(file, delimiter='\t', quoting=csv.QUOTE_ALL)
    writer.writerows(data_to_write)
