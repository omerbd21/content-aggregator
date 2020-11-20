from __future__ import absolute_import

from datetime import datetime

import requests
from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from django.http import JsonResponse

from src.trydjango.settings import SERVICES_URLS

celery_logger = get_task_logger('celery-task')


@shared_task
def get_website_from_mongo(website_name):
    website_request = requests.get(url=SERVICES_URLS['mongo-fetcher'] + "/last_update/" + website_name)
    current_time = datetime.now()
    last_update = datetime.strptime(website_request.text,
                                             "%a, %d %b %Y %H:%M:%S GMT").timetuple()
    time_difference = current_time - last_update
    if divmod(time_difference.total_seconds(), 60)[0] > 4:
        return False  # That means that the MongoDB isn't updated and we need to update it
    website_request = requests.get(url=SERVICES_URLS['mongo-fetcher'] + "/headlines/" + website_name)
    website = website_request.json()
    return JsonResponse(website, json_dumps_params={'ensure_ascii': False})


@shared_task
def get_website_from_content_aggregator(website_name):
    website_request = requests.get(url=SERVICES_URLS['content-aggregator'] + "/" + website_name + ".co.il")
    website = website_request.json()
    return JsonResponse(website, json_dumps_params={'ensure_ascii': False})


@shared_task
def update_website_in_mongo(website_info):
    requests.put(url=SERVICES_URLS['content-aggregator'] + "/update",
                 data=website_info)
