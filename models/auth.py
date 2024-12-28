from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

from dataclasses_json import dataclass_json
from pytimeparse2 import parse
from datetime import datetime, timedelta

DEFAULT_EXPIRY = "7d"


@dataclass_json
@dataclass
class User:
    uid: int
    username: str
    password: str


@dataclass_json
@dataclass
class UserToken(User):
    expiry: datetime


@dataclass
class LoginPayload:
    username: str
    password: str
    expiry: str


@dataclass
class RegisterPayload:
    username: str
    email: str
    password: str
    registration_token: str
