import jwt
from sanic import Blueprint, Request, json
from sanic_ext import validate
from models.auth import LoginPayload, RegisterPayload, User
from models.main import APIResponse

auth_bp = Blueprint("auth", url_prefix="/auth")


@auth_bp.post("/login")
@validate(json=LoginPayload)
async def login(request: Request, body: LoginPayload):
    user_query = await request.app.ctx.db.execute(
        "SELECT uid, username, password FROM users WHERE username = ? LIMIT 1;",
        [body.username]
    )

    if not len(user_query.rows) > 0:
        return json(APIResponse(success=False, message="Username not found"))
    
    try:
        user = User(*user_query[0])
        token = jwt.encode(user.to_dict(), request.app.config.SECRET, algorithm="HS256")
        return json(APIResponse(success=True, message="Login succesful", data={"token": token}))
    
    except:
        return json(APIResponse(success=False, message="Internal server error"))
    
@auth_bp.post("/register")
@validate(json=RegisterPayload)
async def register(request: Request, body: RegisterPayload): ...
