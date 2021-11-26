import json

data = {
    "president": {
        "species": "Betelgeusian",
        "name": "Zaphod Beeblebrox"
    }
}

with open('data_file.json', 'w') as file:
    json.dump(data, file, indent=4, sort_keys=True)  # сериализация (передаваемые данные, непосредственно файл, отступы)

print(json.dumps(data, indent=4))  # сериализация (сохранение в json-строку)


with open('data_file.json', 'r') as file:
    new_data = json.load(file)  # десериализация
print(new_data)

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

data1 = json.loads(json_string)  # десериализация
print(data1)