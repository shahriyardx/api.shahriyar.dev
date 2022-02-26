from quart import Blueprint

from .urls import url_patterns

disstatus = Blueprint("disstatus", __name__, url_prefix="/disstatus")

for path in url_patterns:
    disstatus.add_url_rule(
        rule=path.url, view_func=path.view_func, methods=path.methods
    )
