from flask import render_template, request
from project.database import db, Recipes, Ingredients, Book
import time


class Searcher:

    @classmethod
    def intersect_recipes(cls, all_r):
        result = db.intersect(*all_r)
        return result

    @classmethod
    def search_recipes_new(cls, search_elements):
        all_found_recipes = []
        for ing in search_elements:
            rec = db.session.query(Recipes).join(Book, Book.recipe_id == Recipes.id).join(
                Ingredients, Book.ingredient_id == Ingredients.id).filter(
                Ingredients.ingredient.ilike(f'%{ing.strip()}%'))
            all_found_recipes.append(rec)

        return all_found_recipes

    @classmethod
    def get_search_elem(cls, q):
        search_elem = q.split(',')
        return search_elem

    # @classmethod
    # def search_ingredient(cls, ing):
    #     ingredient = Ingredients.query.filter(Ingredients.ingredient.ilike(f'%{ing.strip()}%')).first()
    #     return ingredient
    #
    # @classmethod
    # def search_id_recipes(cls, search_elements):
    #     ids = []
    #     temp_ids = []
    #     for ing in search_elements:
    #         ingredient = cls.search_ingredient(ing)
    #         if ingredient is None:
    #             return None
    #
    #         if not ids:
    #             for j in ingredient.book:
    #                 ids.append(j.recipe_id)
    #         elif ids:
    #             for j in ingredient.book:
    #                 temp_ids.append(j.recipe_id)
    #             ids = list(set(ids) & set(temp_ids))
    #
    #     return ids
    #
    # @classmethod
    # def search_recipes(cls, ids):
    #     recipes = []
    #     for i in ids:
    #         recipe = Recipes.query.get(i)
    #         recipes.append(recipe)
    #
    #     return recipes


class Handler:
    @classmethod
    def index(cls):
        recipes = Recipes.query.order_by(Recipes.id.desc()).limit(5).all()
        return render_template('index.html', recipes=recipes)

    @classmethod
    def search(cls):
        q = request.args.get('q')
        if q:
            search_elements = Searcher.get_search_elem(q)
            all_found_recipes = Searcher.search_recipes_new(search_elements)
            query = Searcher.intersect_recipes(all_found_recipes)
            recipes = db.session.execute(query)
            print(recipes.first()['recipes_title'])

            # СТАРЫЙ ----------------------------------------------
            # search_elements = Searcher.get_search_elem(q)
            # start_time = time.perf_counter()
            #
            # ids = Searcher.search_id_recipes(search_elements)
            #
            # if ids is None:
            #     # flash('Не найдено')
            #     return render_template('search.html', title='Поиск')
            #
            # recipes = Searcher.search_recipes(ids)
            # # print(recipes[0])
            #
            # print(f'Время: {time.perf_counter() - start_time}')

            return render_template('search.html', title='Поиск')
