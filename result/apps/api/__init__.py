from quart import Blueprint

from .urls import url_patterns

api = Blueprint("api", __name__, url_prefix="/api")

for path in url_patterns:
    api.add_url_rule(rule=path.url, view_func=path.view_func, methods=path.methods)

from .errors import *
