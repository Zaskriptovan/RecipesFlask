from project import app
from project.handler import Handler


class Router:
    app.add_url_rule('/', view_func=Handler.index, methods=['POST', 'GET'])