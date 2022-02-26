from dotenv import load_dotenv
from quart import Quart
from quart_cors import cors

from .apps.result import result_api
from .apps.disstatus import disstatus
from .config import config
from .helpers.result import ResultParser
from .urls import url_patterns

load_dotenv(".env")
app = Quart(__name__)

cors(app, allow_origin="*")

app.config.from_object(
    config["production"]
)  # Change it to production for production use

app.results = ResultParser().get_all_result()
app.result_cache = dict()

app.register_blueprint(result_api)
app.register_blueprint(disstatus)

for path in url_patterns:
    app.add_url_rule(rule=path.url, view_func=path.view_func, methods=path.methods)
