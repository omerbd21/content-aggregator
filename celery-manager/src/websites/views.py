import requests
from django.http import HttpResponse, JsonResponse

import sys
sys.path.insert(0, '../src/trydjango')
from trydjango.settings import SERVICES_URLS


# Getting website input from content-aggregator
def get_website(request,website_name):
    website_request = requests.get(url=SERVICES_URLS['content-aggregator']+"/"+website_name)
    website = website_request.json()
    return JsonResponse(website, json_dumps_params={'ensure_ascii': False})
