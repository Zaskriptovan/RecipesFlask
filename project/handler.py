from flask import render_template, request
from project.database import Recipes


class Handler:

    @classmethod
    def index(cls):
        recipes = Recipes.query.order_by(Recipes.id.desc()).limit(3).all()

        return render_template('index.html', recipes=recipes)
