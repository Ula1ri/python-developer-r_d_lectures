from .models import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer, nullable = False)

class Publishing_house(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ratind = db.Column(db.Integer, default=5)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    year = db.Column(db.Integer, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    Publishing_house_id =db.Column(db.Integer, db.ForeingKey('publishing_house.id'), nullable = False)
    publishing_house = db.relationship('Publishing_house')

class Purchases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeingKey('user.id'), nullable = False)
    user = db.relationship('User')
    books_id = db.Column(db.Integer, db.ForeingKey('books.id'),primary_key=True)
    books = db.relationship('Books')