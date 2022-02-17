from quart import Quart
from quart_cors import cors

from .apps.api import api
from .config import config
from .helpers.result import ResultParser
from .urls import url_patterns

app = Quart(__name__)
app.results = ResultParser().get_all_result()

cors(app, allow_origin="*")

app.config.from_object(config["development"])  # Change it to production for production use

app.register_blueprint(api)

for path in url_patterns:
    app.add_url_rule(rule=path.url, view_func=path.view_func, methods=path.methods)
