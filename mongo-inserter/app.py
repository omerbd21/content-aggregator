from flask import Flask, Response

from api import website
from connection import connect_mongo

app = Flask(__name__)

app.register_blueprint(website)

with app.app_context():
    connect_mongo()


@app.route('/')
def index():
    return Response("You're in the mongo-inserter", 200)


def run():
    app.run(host='0.0.0.0', port=8080)
