from dataclasses import dataclass
from typing import Optional
from pytimeparse2 import parse
from datetime import datetime, timedelta

DEFAULT_EXPIRY = "7d"


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
