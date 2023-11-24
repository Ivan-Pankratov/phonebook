from phone_functions import *

phonebook = {}

while True:
    command = input("Введите команду \n(для справки: /help) ")
    if command == "/all":                     # Печать справочника в консоль
        print_info(phonebook)
    elif command == "/stop":                  # Прерывание программы с записью
        save(phonebook)
        print("Бот остановил свою работу. Заходите ещё, будем рады!")
        break
    elif command == "/add" :                 #Добавление записи
        add_info(phonebook)
    elif command == "/help":                 # Вывод мануала
        help_info()
    elif command == "/delete":               # Удаление контакта из списка
        delete_info(phonebook)
    elif command == "/change":               # Изменение контакта в списке
        change_info(phonebook)
    elif command == "/find":                 # Поиск контакта
        find_info(phonebook)
    elif command == "/save" :                # Экспорт/Сохранение справочника
        save(phonebook)
    elif command == "/load":                 # Импорт/Загрузка справочника из хранилища
        phonebook= load(phonebook)
    else:
        print("Неопознанная команда. Просьба изучить мануал через /help")