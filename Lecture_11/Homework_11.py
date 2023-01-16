# 1 Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана.
# Декоратор має працювати для різних функцій однаково.

# 2 Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occurred".

# 3 Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 10 знаків дорівнює перед
# виконанням коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює.

# 4 У випадку виникнення будь-якої помилки вона має бути надрукована текстом,
# проте програма не має завершити своєї роботи.

# 5 Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж,
# що і менеджер контексту із попереднього завдання.

# 6 Додати обробку помилок до коду із попередніх домашніх завдань (необов'язкове виконання)

from datetime import datetime
from contextlib import contextmanager

class MyCustomException(Exception):
    pass


class MyContextManager():
    def __int__(self, value):
        self.value = value

    def __enter__(self):
        print('==========')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == Exception:
            print(f'{exc_val} We have same situation here!')

        print('==========')
        return True


def my_deco_log(func):
    def wrap(*args, **kwargs):
        with MyContextManager() as file:
            print(f'Function {func} is called at {datetime.now()}')
            func()
            raise MyCustomException('Custom exception is occurred')

    return wrap()


@my_deco_log
def my_func():
    print('my_func')


try:
    print('==========')
    wrong_var = 1 / 0
except Exception as lol:
    print(f'Custom exception is occurred: {lol}')
except:
    raise MyCustomException('Custom exception is occurred')
finally:
    print(f'Function {Exception} is called at {datetime.now()}')
    print('==========')