from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class Path:
    url: str
    view_func: Any
    methods: List[str] = field(default_factory=lambda: ["GET"])
