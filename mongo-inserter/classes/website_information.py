import mongoengine as mongoengine

from classes import MainHeadline


class WebsiteInformation(mongoengine.EmbeddedDocumentField):
    name = mongoengine.StringField(required=True)
    main_headline = mongoengine.EmbeddedDocumentField(MainHeadline, required=True)
    minor_headlines = mongoengine.ListField(mongoengine.StringField, required=True)
