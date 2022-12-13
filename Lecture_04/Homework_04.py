# 1. Створити програму, яка буде очікувати введення тексту від користувача
#  і повідомляти — чи є введений текст “числом” чи “словом”. 

#2. Якщо введений текст “число”, програма має також вказати
#  чи є воно парним чи непарним. 

#3. Якщо це “слово”, програма має вказати його довжину.

some_text = input("Write me something, please: ")
if some_text.isdigit():
    some_text = int(some_text)
    if some_text % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")
else:
    some_text = len(some_text)
    print(f'This word have {some_text} letter')