from flask_sqlalchemy import SQLAlchemy
from project import app

db = SQLAlchemy(app)


class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)

    ingredients = db.relationship('Ingredients', backref='recipe')

    def __repr__(self):
        return f'id: {self.id}, title: {self.title}'


class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.Text, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))

    def __repr__(self):
        return f'{self.ingredient}'
