from pytimeparse2 import parse
from models.auth import DEFAULT_EXPIRY
from datetime import datetime, timedelta
from models.main import APIResponse
from sanic import json
from sanic.response.convenience.json import JSONResponse


def successful(
    message: str, data: dict | None = None, response_code: int = 200
) -> JSONResponse:
    response = APIResponse(succesful=True, message=message, data=data)
    return json(response, response_code)


def unsuccessful(
    message: str, data: dict | None = None, response_code: int = 400
) -> JSONResponse:
    response = APIResponse(succesful=False, message=message, data=data)
    return json(response, response_code)


def timestamp_expired(ts: int | float) -> bool:
    try:
        current_time = datetime.now()
        timestamp_time = datetime.fromtimestamp(ts)
        return timestamp_time < current_time

    except (OverflowError, OSError) as e:
        print(
            f"Error processing timestamp {ts}\n{e}"
        )  # TODO: Replace with proper logging
        return True


def expiry_date(exp: int | float) -> datetime:
    try:
        d = datetime.fromtimestamp(exp)
        return d

    except OverflowError as e:
        print(f"Invalid timestamp {exp}\n{e}")  # todo: proper logging

    except OSError as e:
        print(f"OS error occured trying to parse {exp}\n{e}")

    return datetime.now() - timedelta(hours=8)  # Make sure the token is long invalid


def parse_expiry(exp: str) -> datetime:
    parsed = parse(exp)

    if not isinstance(parsed, int | float):
        return parse_expiry(DEFAULT_EXPIRY)

    return expiry_date(parsed)
