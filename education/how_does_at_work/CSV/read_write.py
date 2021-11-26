import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]

# with open('read_write.csv', 'w', encoding='cp1251', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     for row in data:
#         writer.writerow(row)

with open('read_write.csv', 'w', encoding='cp1251', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(data)  # writerows можно передать любой итерируемый объект

with open('read_write.csv', 'r', encoding='cp1251') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)
