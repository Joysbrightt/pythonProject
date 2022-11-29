import json

config_dict = {"name": "Adeola",
               "age": 18,
               1: "Birthday",
               "hobby": [1, 2, 3, 4],
               "bool": True}

with open("config.json", mode="w+") as temp_file:
    json.dump(config_dict, temp_file, indent=4, separators=(',', ':'))
with open("config.json", mode="r+") as temp_file:
    con = json.load(temp_file)
    print(temp_file)


j = json.dumps(config_dict)
print(type(j))
print(j)