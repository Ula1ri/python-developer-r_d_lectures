# 1. Створити програму, яка буде очікувати від користувача введення тексту 
# і виведе інформацію по кожному надрукованому символу: 
# це “число” + яке воно (парне, непарне), 
# це “буква” + яка вона (велика чи маленька),
# це “символ”

s = input('Write me something, please: ')
for item in s:
    if item.isdigit():
        item = int(item)
        if item % 2 == 0:
            print(f'{item} - this number is even')
        else:
            print(f'{item} - this number is odd')
    elif item.isupper():
        print(f'{item} - this letter is in upper case')
    elif item.islower():
        print(f'{item} - this letter is in lower case')
    else:
        print(f'{item} - this is symbol')