import json

import requests
from django.http import HttpResponse, JsonResponse

import sys

sys.path.insert(0, '../trydjango')
from src.trydjango.settings import SERVICES_URLS


# TODO : Get website list from mongo
def get_website_names(request):
    websites_request = requests.get(url=SERVICES_URLS['mongo-fetcher'] + "/names")
    website_names = websites_request.json()
    return JsonResponse(website_names, safe=False)
# TODO : Change get_website to first check in MONGO and then get from content-aggregator and update the DB
# Add Celery
