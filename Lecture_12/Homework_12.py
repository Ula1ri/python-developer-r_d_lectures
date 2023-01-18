# 1. Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.

# Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
# При закритті програми і повторному відкритті всі попередні дані мають бути доступними.
# Підказка: Ви можете використати бібліотеку json, яка допоможе із перетворенням dict в JSON string (при записі в файл)
# і JSON string в dict (при читанні із файлу). Файл слід оновлювати після кожної успішної операції add або delete.

# 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.

# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.

import json
from datetime import datetime


class MyCustomException(Exception):
    with open('log.txt', 'a') as log_file:
        print(f'\nFunction {Exception} is called at {datetime.now()}', file=log_file) # записуємо в log.txt виклик функції
    pass

def my_deco(func):
    def wrap(*args, **kwargs):
        with open('log.txt', 'a') as log_file:
            print(f'\nFunction {open} is called at {datetime.now()}', file=log_file) # записуємо в log.txt виклик функції
        func(*args, **kwargs)
        return func(*args, **kwargs)
    wrap

@my_deco
def my_func():
    print('my_func')

with open('json_dict.txt',) as phone_data: #Зчитємо дані з файла
    phone_file = phone_data.read()
    phone_book = json.loads(phone_file) # перетворюємо jsonstring в dict
while True:
    input_data = input('Please, enter new command: ')  # format "command name number" commands: stats, add, delete,
    # list, show
    split_input = input_data.split()

    command = split_input[0]
    if len(split_input) > 1:
        name = split_input[1]
    if len(split_input) > 2:
        number = split_input[2]

    if command == 'stats':
        print(len(phone_book))
    elif command == 'add':
        if name in phone_book.keys():
            print('This name is already in use, please enter another one')
        else:
            phone_book[name] = number
            phone_book = json.dumps(phone_book)
            with open('json_dict.txt', 'w') as file:  # додаэмо дані в файл словника
                file.write(phone_book)
    elif command == 'delete':
        if name in phone_book.keys():
            phone_book.pop(name)
            phone_book = json.dumps(phone_book)
            with open('json_dict.txt', 'w') as file:  # перезаписуємао файл з словником
                file.write(phone_book)
    elif command == 'list':
        try:
            for key in phone_book.keys():
                print(key)
        except:    
            raise MyCustomException()
    elif command == 'show':
        if name in phone_book:
            print(phone_book[name])
