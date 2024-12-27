from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

from dataclasses_json import dataclass_json
from pytimeparse2 import parse

DEFAULT_EXPIRY = "7d"


@dataclass_json
@dataclass
class User:
    uid: int
    username: str
    password: str


@dataclass
class LoginPayload:
    username: str
    password: str
    expiry: Optional[str] | datetime

    def __post_init__(self):
        if not isinstance(self.expiry, str):
            self.expiry = DEFAULT_EXPIRY

        try:
            expirySeconds = parse(self.expiry)
            if not expirySeconds:
                raise

            self.expiry = datetime.now() + timedelta(seconds=expirySeconds)

        except:
            self.expiry = DEFAULT_EXPIRY


@dataclass
class RegisterPayload:
    username: str
    email: str
    password: str
    registration_token: str
