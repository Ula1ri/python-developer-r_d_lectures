import re

phone_book = {
    'Taras': '+380123456789',
    'Dmutro': '+380123456790',
    'Kevin': '+380123456791',
    'Peter': '+380123456792',
}
while True:
    input_data = input('Please, enter new command: ')  # format "command name number" commands: stats, add, delete,
    # list, show
    split_input: list[str] = input_data.split()

    command = split_input[0]
    if len(split_input) > 1:
        name = split_input[1]
    if len(split_input) > 2:
        number = split_input[2]

        match = re.findall(r"(?:\+?38|8)?0\d{9}(?=[, ]|$)", number)

    if command == 'stats':
        print(len(phone_book))
    elif command == 'add':
        if name in phone_book.keys():
            print('This name is already in use, please enter another one')
        elif match:
            phone_book[name] = number
        else:
            print(f'{number} number is incorrect')
    elif command == 'delete':
        if name in phone_book.keys():
            phone_book.pop(name)
    elif command == 'list':
        for key in phone_book.keys():
            print(key)
    elif command == 'show':
        if name in phone_book:
            print(phone_book[name])