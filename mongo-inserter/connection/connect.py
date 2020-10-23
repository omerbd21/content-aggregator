from mongoengine import connect

from settings import DB_NAME, USER, DB_HOST, ALIAS


def connect_mongo():
    connect(
        db=DB_NAME,
        username=USER,
        password='Password1',
        host=DB_HOST,
        alias=ALIAS
    )
