from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

from routes.feed_routes import *
from routes.auth_routes import *

if __name__ == "__main__":
    app.run()