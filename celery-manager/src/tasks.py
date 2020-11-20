from __future__ import absolute_import

import json
import time
from datetime import datetime

import requests
from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from django.http import JsonResponse

from src.trydjango.settings import SERVICES_URLS, MINUTES_DIVIDER

celery_logger = get_task_logger('celery-task')


@shared_task
def get_website_from_mongo(website_name):
    try:
        website_request = requests.get(url=SERVICES_URLS['mongo-fetcher'] + "/last_update/" + website_name)
        current_time = datetime.now()
        last_update = datetime.strptime(website_request.text[1:-1],
                                        "%m/%d/%Y, %H:%M:%S").timetuple()
        time_difference = time.mktime(datetime.timetuple(current_time)) - time.mktime(last_update)
        if time_difference / MINUTES_DIVIDER > 4:
            return False  # That means that the MongoDB isn't updated and we need to update it
    except ValueError:
        return False  # That means there is no entry in the DB
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
    headers = {'content-type': 'application/json'}
    code = requests.put(url=SERVICES_URLS['mongo-inserter'] + "/update",
                        data=json.dumps(website_info), headers=headers)
    print(code.headers['content-type'])
