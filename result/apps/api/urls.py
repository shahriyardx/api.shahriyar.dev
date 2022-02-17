from ...helpers.models import Path
from .views import result

url_patterns = [
    Path("/result/<int:roll>/", result, ["GET"]),
]
