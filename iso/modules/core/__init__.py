from quart import Blueprint
from iso.utils import render


core = Blueprint("core", __name__)


@core.route("/")
async def index():
    return await render("app/index.html", {"title": ":^)"})


