from os import getenv

from dotenv import load_dotenv
from sanic import Sanic
from sanic.worker.manager import WorkerManager

from src.database import Turso
from routes.auth import auth_bp
from routes.main import main_bp

WorkerManager.THRESHOLD = 600

# To implement:
# Use Nginx as proxy for access logging, Python's logging is slow
# run sanic with --no-access-logs flag

load_dotenv()

TURSO_URL = getenv("TURSO_URL")
TURSO_TOKEN = getenv("TURSO_TOKEN")
APP_SECRET = getenv("APP_SECRET")

app = Sanic("PyAPI")
#app.config.REQUEST_MAX_SIZE = 10000000 # 1mb
#app.config.REQUEST_TIMEOUT = 30 # seconds

app.blueprint(main_bp)
app.blueprint(auth_bp)
app.config.KEEP_ALIVE_TIMEOUT = 15  # seconds
app.config.SECRET = APP_SECRET

turso = Turso(TURSO_URL, TURSO_TOKEN)

# Health endpoint (__health__) is not secured out of the box.
# https://sanic.dev/en/plugins/sanic-ext/health-monitor.html#getting-started
# Add some type of route securing (depending on health use-case) in the end host environment
# app.config.HEALTH = True
# app.config.HEALTH_ENDPOINT = True


@app.before_server_start
async def attach_db(app, loop):
    app.config.REQUEST_MAX_SIZE = 10000000 # 1mb
    app.config.REQUEST_TIMEOUT = 30 # seconds
    app.ctx.db = await turso.get_client()
