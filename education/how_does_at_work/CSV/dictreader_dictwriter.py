import csv

data = [{
    'hostname': 'sw1',
    'location': 'London',
    'model': '3750',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw2',
    'location': 'Liverpool',
    'model': '3850',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw3',
    'location': 'Liverpool',
    'model': '3650',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw4',
    'location': 'London',
    'model': '3650',
    'vendor': 'Cisco'
}]

with open('read_write.csv', 'r', encoding='cp1253', newline='') as file:
    reader = csv.DictReader(file, delimiter=';')
    for line in reader:
        print(line)

with open('dictwriter_dictreader.csv', 'w', encoding='cp1253', newline='') as file2:
    header = ['hostname', 'vendor', 'model', 'location']
    writer = csv.DictWriter(file2, delimiter=';', fieldnames=header)
    writer.writeheader()
    for line2 in data:
        writer.writerow(line2)
