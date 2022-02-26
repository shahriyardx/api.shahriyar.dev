from ...helpers.types import Path
from .views import result

url_patterns = [
    Path("/<int:roll>/", result, ["GET"]),
]
