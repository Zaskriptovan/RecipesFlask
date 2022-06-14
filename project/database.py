from flask_sqlalchemy import SQLAlchemy
from project import app

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'))
    quantity_id = db.Column(db.Integer, db.ForeignKey('quantity.id'))

    # __table_args__ = (db.UniqueConstraint(recipe_id, ingredient_id, quantity_id),)

    recipe = db.relationship('Recipes', back_populates='book')
    ingredient = db.relationship('Ingredients', back_populates='book')
    quantity = db.relationship('Quantity', back_populates='book')

    def __repr__(self):
        return f'{self.ingredient} — {self.quantity}'


class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)

    book = db.relationship('Book', back_populates='recipe')

    def __repr__(self):
        return f'id: {self.id} title: {self.title}'


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
