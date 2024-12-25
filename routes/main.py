# Routes for the top level
from sanic.response import json
from sanic.request import Request
from sanic import Blueprint

main_bp = Blueprint("main_blueprint")


@main_bp.route("/")
async def root(request: Request):
    return json({"test": "route"})
