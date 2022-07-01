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


class Handler:
    @classmethod
    def index(cls):
        recipes = Recipes.query.order_by(Recipes.id.desc()).limit(5).all()
        return render_template('index.html', recipes=recipes)

    @classmethod
    def search(cls):
        q = request.args.get('q')
        if q:
            search_elements = Searcher.get_search_elements(q)
            all_found_recipes_id = Searcher.search_recipes_id_by_ingredients(search_elements)
            intersect_recipes_id = Searcher.intersect_recipes_id(all_found_recipes_id)
            recipes = Searcher.search_for_recipe_matches(intersect_recipes_id)

            if not recipes:
                flash('НЕ НАЙДЕНО')

            return render_template('search.html', recipes=recipes, title='Поиск')
