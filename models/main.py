from dataclasses import dataclass
from typing import Optional, TypedDict


@dataclass
class InputValidation:
    q: str


class APIResponse(TypedDict):
    success: bool
    message: Optional[str]
    data: Optional[dict]
