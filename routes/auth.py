import jwt
from sanic import Blueprint, Request, json
from sanic_ext import validate
from models.auth import LoginPayload, RegisterPayload

auth_bp = Blueprint("auth", url_prefix="/auth")


@auth_bp.post("/login")
@validate(json=LoginPayload)
async def login(request: Request, body: LoginPayload):
    return json({"ok": True})

@auth_bp.post("/register")
@validate(json=RegisterPayload)
async def register(request: Request, body: RegisterPayload):
    ...
