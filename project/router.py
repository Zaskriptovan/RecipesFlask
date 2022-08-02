from project import app
from project.handler import Handler


class Router:
    app.add_url_rule('/', view_func=Handler.index, methods=['POST', 'GET'])
    app.add_url_rule('/search/<ing>', view_func=Handler.search, methods=['POST', 'GET'])
    app.add_url_rule('/<recipe_id>', view_func=Handler.recipe_details, methods=['POST', 'GET'])
    app.add_url_rule('/about', view_func=Handler.about, methods=['POST', 'GET'])
    app.add_url_rule('/live-search', view_func=Handler.live_search, methods=['POST', 'GET'])
