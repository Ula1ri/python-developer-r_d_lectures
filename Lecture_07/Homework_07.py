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
    input_data = input('Please, enter new command: ')  # format "command name number" commands: stats, add, delete,
    # list, show
    split_input = input_data.split()

    command = split_input[0]
    name = split_input[1]
    number = split_input[2]

    if command == 'stats':
        print(len(phone_book))
    elif command == 'add':
        if name in phone_book.keys():
            print('This name is already in use, please enter another one')
        else:
            phone_book[name] = number
    elif command == 'delete':
        if name in phone_book.keys():
            phone_book.pop(name)
    elif command == 'list':
        for key in phone_book.keys():
            print(key)
    elif command == 'show':
        if name in phone_book:
            print(phone_book[name])
