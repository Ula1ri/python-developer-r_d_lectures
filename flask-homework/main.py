import logging
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Налаштування логування
logging.basicConfig(filename='flask.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

# Ендпоінт "hello"
@app.route('/hello')
def hello():
    app.logger.info('Hello endpoint was reached')
    return 'Hello, world!'

# Обробник запитів GET /users
@app.route('/users', methods=['GET'])
def get_users():
    # Рандомний список імен
    names = ['Alice', 'Bob', 'Besil', 'Petro', 'Taras', 'Franklin']
    return ', '.join(names)

# Обробник запитів GET /books
@app.route('/books', methods=['GET'])
def get_books():
    # Рандомний список книжок у вигляді HTML списку
    books = ['Harry Potter', 'Lord of the Rings', 'The Great Gatsby', 'Kobzar']
    books_html = '<ul>' + ''.join(f'<li>{book}</li>' for book in books) + '</ul>'
    return books_html

# Обробник запитів GET /users/:id
@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    # Якщо id ділиться на 2 - повертаємо текст із цим значенням
    # Якщо не ділиться – повертаємо статус 404 Not Found
    if id % 2 == 0:
        return f'The id is {id}'
    else:
        return 'Not found', 404

# Обробник запитів GET /books/:title
@app.route('/books/<title>', methods=['GET'])
def get_book_by_title(title):
    # Трансформуємо першу літеру title у велику, а всі інші у маленькі
    transformed_title = title.capitalize()
    return transformed_title

# Обробник запитів GET /params
@app.route('/params', methods=['GET'])
def get_params():
    # HTML таблиця з ключами та значеннями query parameters
    params = request.args.items()
    params_table = '<table><tr><th>parameter</th><th>value</th></tr>'
    for key, value in params:
        params_table += f'<tr><td>{key}</td><td>{value}</td></tr>'
    params_table += '</table>'
    return params_table

# Обробник запитів GET, POST /login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Якщо запит GET - повертаємо форму для вводу імені користувача та пароля
    if request.method == 'GET':
        return render_template('login.html')
    # Якщо запит POST - перевіряємо ім'я користувача та пароль
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Якщо дані є, перенаправляємо користувача на сторінку
        if username == 'admin' and password == 'admin':
            return redirect('/')
        else:
            return render_template('login_error.html')

if __name__ == '__main__':
    app.run()