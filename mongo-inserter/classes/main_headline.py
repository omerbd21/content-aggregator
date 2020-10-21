import mongoengine as mongoengine


class MainHeadline(mongoengine):
    text = mongoengine.StringField(required=True)
    url = mongoengine.URLField(required=True)
