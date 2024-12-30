import jwt
from sanic import Blueprint, Request
from sanic_ext import validate
from src.auth import password_match
from models.auth import LoginPayload, RegisterPayload, UserToken
from src.addon import parse_expiry, timestamp_expired, successful, unsuccessful

auth_bp = Blueprint("auth", url_prefix="/auth")


@auth_bp.post("/login")
@validate(json=LoginPayload)
async def login(request: Request, body: LoginPayload):
    user_query = await request.app.ctx.db.execute(
        "SELECT uid, username, password FROM users WHERE username = ? LIMIT 1;",
        [body.username],
    )

    if not len(user_query.rows) > 0:
        return unsuccessful("Username not found", response_code=404)

    user_object = user_query[0]
    if not password_match(body.password, user_object[2]):
        return unsuccessful("Login unsuccessful", response_code=404)
    try:
        user = UserToken(*user_object, expiry=parse_expiry(body.expiry).timestamp())
        token = jwt.encode(user.to_dict(), request.app.config.SECRET, algorithm="HS256")
        return successful("Login successful", data={"token": token})

    except Exception as e:
        print(f"Unknown exception occured during login request {e}")
        return unsuccessful("Internal server error", response_code=500)


@auth_bp.post("/register")
@validate(json=RegisterPayload)
async def register(request: Request, body: RegisterPayload):
    rtoken_query = await request.app.ctx.db.execute(
        "SELECT id, token, expiry FROM registration_tokens WHERE token = ? LIMIT 1;",
        [body.registration_token],
    )

    if len(rtoken_query.rows) == 0:
        return unsuccessful("Invalid registration token", response_code=404)

    id, token, expiry = rtoken_query.rows[0]
    if timestamp_expired(expiry):
        
        return unsuccessful("Expired registration token", response_code=404)
