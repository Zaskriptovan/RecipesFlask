from flask_sqlalchemy import SQLAlchemy
from project import app

db = SQLAlchemy(app)

ingredients_recipes = db.Table('ingredients_recipes',
                               db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id')),
                               db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.id')))


class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)

    # ingredients = db.relationship('Ingredients', secondary=recipe_ingredients, backref='recipe')

    def __repr__(self):
        return f'id: {self.id}, title: {self.title}'


class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.Text, nullable=False)

    recipe = db.relationship('Recipes', secondary=ingredients_recipes, backref='ingredients')

    def __repr__(self):
        return f'{self.ingredient}'
