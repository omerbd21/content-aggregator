from mongoengine import connect

from settings import DB_HOST


def connect_mongo():
    connect(
        host=DB_HOST
    )
