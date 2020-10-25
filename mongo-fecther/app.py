from api import website
from connection import connect_mongo
from flask import Response, Flask

app = Flask(__name__)

app.register_blueprint(website)

with app.app_context():
    connect_mongo()


@app.route('/')
def index():
    return Response("You're in the mongo-fetcher", 200)


def run():
    app.run(host='0.0.0.0', port=8080)
