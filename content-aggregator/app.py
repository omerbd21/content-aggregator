from flask import Flask, Response

from api import website

app = Flask(__name__)

app.register_blueprint(website)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return Response("You're in the content aggregator API!", 200)


def run():
    app.run(host='0.0.0.0', port=8080)
