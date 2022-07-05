from flask import render_template, request, flash
from project.database import db, Recipes, Ingredients, Book


class Searcher:
    @classmethod
    def search_for_recipe_matches(cls, intersect_recipes_id):
        recipes = Recipes.query.filter(Recipes.id.in_(intersect_recipes_id)).all()
        return recipes

    @classmethod
    def intersect_recipes_id(cls, recipes_id):
        result = db.intersect(*recipes_id)
        return result

    @classmethod
    def search_recipes_id_by_ingredients(cls, search_elements):
        all_found_recipes_id = []
        for ing in search_elements:
            rec = db.session.query(Recipes.id) \
                .join(Book, Book.recipe_id == Recipes.id) \
                .join(Ingredients, Book.ingredient_id == Ingredients.id) \
                .filter(Ingredients.ingredient.ilike(f'%{ing}%'))
            all_found_recipes_id.append(rec)

        return all_found_recipes_id

    @classmethod
    def get_search_elements(cls, q):
        search_elements = [x.strip() for x in q.split(',')]
        return search_elements

    @classmethod
    def result(cls, q):
        search_elements = cls.get_search_elements(q)
        all_found_recipes_id = cls.search_recipes_id_by_ingredients(search_elements)
        intersect_recipes_id = cls.intersect_recipes_id(all_found_recipes_id)
        recipes = cls.search_for_recipe_matches(intersect_recipes_id)

        return recipes


class Handler:
    @staticmethod
    def index():
        recipes = Recipes.query.order_by(Recipes.id.desc()).limit(20).all()
        return render_template('index.html', recipes=recipes)

    @staticmethod
    def search():
        q = request.args.get('q')
        if q:
            recipes = Searcher.result(q)
            if not recipes:
                flash('НЕ НАЙДЕНО')
            return render_template('search.html', recipes=recipes, title='Поиск')

        else:
            return render_template('search.html', title='Поиск')
