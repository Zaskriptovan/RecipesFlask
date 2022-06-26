from flask_sqlalchemy import SQLAlchemy
from project import app

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'))
    quantity_id = db.Column(db.Integer, db.ForeignKey('quantity.id'))

    recipe = db.relationship('Recipes', back_populates='book')
    ingredient = db.relationship('Ingredients', back_populates='book')
    quantity = db.relationship('Quantity', back_populates='book')

    def __repr__(self):
        return f'Объект ассоц {self.recipe} — {self.ingredient}'


class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)

    book = db.relationship('Book', back_populates='recipe')

    def __repr__(self):
        return f'{self.title}'


class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.Text, nullable=False)

    book = db.relationship('Book', back_populates='ingredient')

    def __repr__(self):
        return f'{self.ingredient}'


class Quantity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Text, nullable=False)

    book = db.relationship('Book', back_populates='quantity')

    def __repr__(self):
        return f'{self.quantity}'
