# Routes for the top level
from sanic import Blueprint
from sanic.request import Request
from sanic.response import json

main_bp = Blueprint("main_blueprint")


@main_bp.route("/")
async def root(request: Request):
    return json({"test": "route"})
