from quart import Quart
from quart_cors import cors

from .helpers.result import ResultParser

from .apps.result import result_api
from .config import config
from .urls import url_patterns

app = Quart(__name__)

cors(app, allow_origin="*")

app.config.from_object(config["production"])  # Change it to production for production use
app.results = ResultParser().get_all_result()
app.result_cache = dict()

app.register_blueprint(result_api)

for path in url_patterns:
    app.add_url_rule(rule=path.url, view_func=path.view_func, methods=path.methods)
