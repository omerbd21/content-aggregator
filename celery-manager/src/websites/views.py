# Your HTML pages
# Here we will put all the requests to backend
import requests
from django.shortcuts import render
from django.http import HttpResponse


def student_show(request):
    # api-endpoint
    URL = "http://content-aggregator-content-aggregator.192.168.5.60.nip.io/website/one.co.il"

    # defining a params dict for the parameters to be sent to the API

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    # extracting data in json format
    data = r.text
    print(data)
    return HttpResponse("<h1>DataFlair Django Tutorials</h1>" + data['main_headline']['text'])
