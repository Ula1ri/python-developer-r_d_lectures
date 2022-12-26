# 1. Створити телефонну книгу, яка матиме наступні команди:

# stats: кількість записів

# add: додати запис

# delete <name>: видалити запис за іменем (ключем)

# list: список всіх імен в книзі

# show <name>: детальна інформація по імені

# Записи не мають повторюватися, заборонено перезаписувати записи, тільки видаляти і додавати заново. 

phone_book = {
    'Taras': '+123456789',
    'Dmutro': '+123456790',
    'Kevin': '+123456791',
    'Peter': '+123456792',
}
while True:
    input_data = input('What do you wish, my lord?: ')  # format "command name number" commands: stats, add, delete,
    # list, show
    split_input = input_data.split()

    command = split_input[0]
    name = split_input[1]
    number = split_input[2]

    if command == 'stats':
        print(len(phone_book))
    elif command == 'add':
        phone_book.update({name: number})
    elif command == 'delete':
        if name == phone_book.keys():
            del phone_book[name]
    elif command == 'list':
        for key in phone_book.items():
            print(key)
    elif command == 'show':
        if name == phone_book.keys():
            print(phone_book[name])
