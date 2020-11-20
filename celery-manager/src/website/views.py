import json

import requests
from django.http import HttpResponse, JsonResponse

import sys

sys.path.insert(0, '../src/trydjango')
from src.trydjango.settings import SERVICES_URLS
from src.tasks import get_website_from_mongo, get_website_from_content_aggregator, update_website_in_mongo


# Getting website input from content-aggregator
def get_website(request, website_name):
    website = get_website_from_mongo(website_name)
    if not website:
        website = get_website_from_content_aggregator(website_name)
        update_website_in_mongo(json.loads(website.content))
    return website
