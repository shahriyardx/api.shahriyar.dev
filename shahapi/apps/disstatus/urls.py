from ...helpers.types import Path
from .views import status

url_patterns = [
    Path("/<int:user_id>/", status, ["GET"]),
]
