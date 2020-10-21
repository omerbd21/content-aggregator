from flask import Blueprint
from headlines import get_all_headlines
from settings import HTTP_PREFIX

website = Blueprint('website', __name__, url_prefix='/website')


@website.route('/<url>')
def get_website(url):
    try:
        website_object = get_all_headlines(HTTP_PREFIX + url)
        website_name = website_object.get_name()
        main_headline = website_object.get_main_headline()
        minor_headlines = website_object.get_minor_headlines()
        website_json = {'website': website_name,
                        'main_headline': main_headline,
                        'minor_headlines': minor_headlines}
        return str(website_json).replace('\\', '')
    except (AttributeError, IndexError):
        return "This website is not supported."
