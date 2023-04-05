import logging
from flask import Flask, request, redirect, render_template, url_for, session
import secrets
import random

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

names = ['Besil', 'Petro', 'Taras', 'Franklin', 'Michael', 'Trevor']
random.shuffle(names)
books = ['Harry Potter', 'Lord of the Rings', 'Ad Astra', 'Kobzar']
random.shuffle(books)

# Налаштування логування
logging.basicConfig(filename='flask.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

# Ендпоінт "hello"
@app.route('/hello')
def hello():
    app.logger.info('Hello endpoint was reached')
    return 'Hello, world!'

# Обробник запитів GET, POST /login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        session['name'] = name 
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

# Головна сторінка
@app.route('/')
def index():
    name = session.get('name')
    if name:
        return render_template('index.html', name=name)
    else:
        return redirect(url_for('login'))

# Обробник запитів GET /users
@app.route('/users', methods=['GET'])
def get_users():
    if 'name' in session:
        return render_template('users.html', name=session['name'], names=names)
    else:
        return redirect(url_for('login'))


# Обробник запитів GET /users/:id
@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    if 'name' in session:
        if id % 2 == 0:
            name = session['name']
            return render_template('user.html', id=id, name=name)
        else:
            return 'Not found', 404
    else:
        return redirect(url_for('login'))

# Обробник запитів GET /books
@app.route('/books', methods=['GET'])
def get_books():
    if 'name' in session:
        return render_template('books.html', name=session['name'], books=books)
    else:
        return redirect(url_for('login'))

# Обробник запитів GET /books/:title
@app.route('/books/<title>', methods=['GET'])
def get_book_by_title(title):
    if 'name' in session:
        name = session['name']
        transformed_title = title.capitalize()
        return render_template('book.html', transformed_title=transformed_title, name=name)
    else:
        return redirect(url_for('login'))

# Обробник запитів GET /params
@app.route('/params', methods=['GET'])
def get_params():
    if 'name' in session:
        name = session['name']
        params = request.args.items()
        params_table = '<table><tr><th>parameter</th><th>value</th></tr>'
        for key, value in params:
            params_table += f'<tr><td>{key}</td><td>{value}</td></tr>'
        params_table += '</table>'
        return render_template('params.html', params_table=params_table, name=name)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()