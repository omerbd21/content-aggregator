import mongoengine as mongoengine
import datetime

from settings import ALIAS, WEBSITE_COLLECTION


class Website(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    url = mongoengine.URLField(required=True)
    last_update = mongoengine.DateTimeField(default=datetime.datetime.now)
    website = mongoengine.DictField(required=True)
    meta = {
        'db_alias': ALIAS,
        'collection': WEBSITE_COLLECTION
    }
