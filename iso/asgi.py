from quart import Quart
from iso.settings import MODULES


app = Quart(__name__, static_url_path="/static", static_folder="/app/static")


@app.route("/static/<path:path>")
async def static_files(path):
    print(path)
    return "hi"

for module in MODULES:
    app.register_blueprint(module)



