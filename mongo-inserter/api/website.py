import datetime

from flask import Blueprint, request, Response

from classes import Website

website = Blueprint('website', __name__)


@website.route('/create', methods=['POST'])
def create_website_entry():
    data = request.json
    new_website = Website(name=data['name'], url=data['url'],
                          website=data['website_information'])
    new_website.save()
    return Response("Entry in.", 200)


@website.route('/update', methods=['PUT'])
def update_headlines():
    print (type(data))
    data = request.json
    name = data['website']
    website_info = {'website': name,
                    'main_headline': data['main_headline'],
                    'minor_headlines': data['minor_headlines']}
    Website.objects(name=name).update(set__website=website_info,
                                      set__last_update=datetime.datetime.now())
    return website_info
