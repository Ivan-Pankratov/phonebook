import json

# Печать мануала
def help_info():
    path = 'manual.txt'
    data = open('manual.txt', 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()

# Добавление записи
def add_info(f):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number1 = input("Введите номер сотового телефона: ")
    phone_number2 = input("Введите номер домашнего телефона: ")
    f[last_name] = {
        "Имя": first_name,
        "Отчество": middle_name,
        "Номер телефона сотовый": phone_number1,
        "Номер телефона домашний": phone_number2
    }
    print("Контакт успешно добавлен в справичник.")

# Удаление контакта в справочнике
def delete_info(f):
    data = input("Введите фамилию контакта, который надо удалить ")
    try:
        f.pop(data)
        print("Контакт успешно удалён")
    except:
        print("Такого контакта нет в справочнике ")

#  Импорт/Загрузка телефона из хранилища
def load(f):
        with open("phonebook.json", "r", encoding="utf-8") as fh:
            f = json.load(fh)
        print("Справочник телефонов успешно загружен")
        return f

# Поиск элемента по ключу
def find_info(f):
    data = input("Введите фамилию для поиска")
    if data in f:
        print(f[data])
    else:
        print("В справочнике нет такого контакта ")

# Изменение контакта в списке
def change_info(f):
    data = input("Введите фамилию для поиска")
    if data in f:
        print(f[data])
        dt = input("Введите параметр, который хотите поменять")
        f[data][dt] = input("Введите новое значение "+ dt)
    else:
        print("В справочнике нет такого контакта ")

# Печать
def print_info(f):
    if f == {}:
        print("Текущий список контактов пуст \n"
              "добавьте запись или загрузите список из хранилища")
    for k, w in f.items():
        print(k, w)

#  Экспорт/Сохранение справочника
def save(f):
    if f== {}:
        print("Вы пытаетесь сохранить пустой справочник, \n "
              "Попытка перезаписи файла остановлена,\n"
              " т.к. это приведёт к потере данных.")
    else:
        with open("phonebook.json", "w", encoding="utf-8") as fh:
            fh.write(json.dumps(f, ensure_ascii=False))
        print("Справочник телефонов успешно сохранен в файле phonebook.json")

