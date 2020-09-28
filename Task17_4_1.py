import json
with open('array.json') as f:
    file_content = f.read()
    data = json.loads(file_content)

#Создаём счётчик i — индекс элемента.
i = 0
while i < len(data):
    data[i] = data[i] + i
    i += 1

with open('array.json', 'w') as f:
    json.dump(data, f)

with open('array.json') as f:
    print(f.read())
