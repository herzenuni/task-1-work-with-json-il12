

# С помощью какой библиотеки в Python 3 можно работать с JSON файлами?

# Импортируйте необходимые библиотеки
import json
# Импортируем модуль json

# pprint позволяет в понятном для человека виде форматировать 'сложные' структуры данных
import pprint
filename = 'data.json'

try:
    with open(filename, encoding='utf-8') as data_file:
        data = json.load(data_file)
        # использовать модуль json и метод для считывания данных: (data_file)
except FileNotFoundError:
    print("Файл не найден! Файл должен называться: {}".format(filename))
    status = 'Файл не найден'

# Вывести в форматированном виде поля:
# company, email, phone, address
for tmp in data:
    print("-------------------------------------")
    print("Компания: {}".format(tmp["company"]))
    print("E-mail: {}".format(tmp["email"]))
    print("Телефон: {}".format(tmp["phone"]))
    print("Адрес: {}".format(tmp["address"]))
