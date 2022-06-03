from flask_sqlalchemy import SQLAlchemy
from project import app

db = SQLAlchemy(app)


class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'id: {self.id}, text: {self.text}'

# class Users(db.Model):
# id = db.Column(db.Integer, primary_key=True)
# email = db.Column(db.String(50), unique=True)
# password = db.Column(db.String(500), nullable=False)
