from quart import Blueprint, current_app

from ...helpers.result import ResultParser
from .urls import url_patterns

result_api = Blueprint("result_api", __name__, url_prefix="/result")

for path in url_patterns:
    result_api.add_url_rule(
        rule=path.url, view_func=path.view_func, methods=path.methods
    )

from .errors import *
