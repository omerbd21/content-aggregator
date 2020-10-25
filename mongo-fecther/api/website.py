from flask import Blueprint, Response, json

from queries import website_names, get_headlines, get_last_update_time

website = Blueprint('website', __name__)


@website.route('/names')
def fetch_names():
    return Response(json.dumps(website_names()), 200)


@website.route('/headlines/<website_name>')
def fetch_headlines(website_name):
    return Response(json.dumps(get_headlines(website_name)), 200)


@website.route('/last_update/<website_name>')
def fetch_last_update(website_name):
    return Response(json.dumps(get_last_update_time(website_name)), 200)
