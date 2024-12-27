from functools import wraps

import jwt
from jwt.exceptions import PyJWTError
from sanic import Request


def check_token(request: Request) -> bool:
    if not request.token:
        return False

    try:
        token = jwt.decode(
            request.token, request.app.config.SECRET, algorithms=["HS256"]
        )

        return True

    except PyJWTError:
        # Log the JWT error
        return False

    except Exception:
        # Log the unexpected exception
        return False


def protected(func):
    def wrapper(f):
        @wraps(f)
        async def decorator(request: Request, *args, **kwargs): ...

        return decorator

    return wrapper(func)
