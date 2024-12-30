from dataclasses import dataclass

from dataclasses_json import dataclass_json

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
    expiry: int | float


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
