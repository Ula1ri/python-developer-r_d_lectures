import logging
from flask import Flask, request, redirect, render_template, url_for, session, jsonify
import secrets
import random
import os
from os import getenv
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from models import User

# Завантажую значення секретного ключа
load_dotenv()
db = SQLAlchemy()

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')
db_url = os.getenv('SQLALCHEMY_DATABASE_URI')
flask_app_host = os.getenv('FLASK_APP_HOST')
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

from models import *

with app.app_context():
    db.create_all()

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
        users = User.query.all()
        return jsonify([user.serialize() for user in users])
    else:
        return redirect(url_for('login'))


# Обробник запитів GET /users/:id
@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    if 'name' in session:
        user = User.query.filter_by(id=id).first()
        if user:
            return jsonify(user.serialize())
        else:
            return 'Not found', 404
    else:
        return redirect(url_for('login'))

# Обробник запитів GET /books
@app.route('/books', methods=['GET'])
def get_books():
    if 'name' in session:
        books = Books.query.all()
        return jsonify([books.serialize() for books in books])
    else:
        return redirect(url_for('login'))

# Обробник запитів GET /books/:title
@app.route('/books/<title>', methods=['GET'])
def get_book_by_title(title):
    if 'name' in session:
        book = Books.query.filter_by(title=title).first()
        if book is not None:
            return jsonify(book.serialize())
        else:
            return 'Book not found', 404
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
    
@app.route('/purchases', methods=['GET'])
def get_purchases():
    if 'name' in session:
        purchases = Purchases.query.all()
        return jsonify([purchase.serialize() for purchase in purchases])
    else:
        return redirect(url_for('login'))

@app.route('/purchases/<int:id>', methods=['GET'])
def get_purchase_by_id(id):
    if 'name' in session:
        purchase = Purchases.query.get(id)
        if purchase:
            return jsonify(purchase.serialize())
        else:
            return 'Not found', 404
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()