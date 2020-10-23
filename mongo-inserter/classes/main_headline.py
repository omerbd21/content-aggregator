import mongoengine as mongoengine


class MainHeadline(mongoengine.EmbeddedDocumentField):
    text = mongoengine.StringField(required=True)
    url = mongoengine.URLField(required=True)
