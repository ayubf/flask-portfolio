import mongoengine as m
import datetime

class Posts(m.Document):
    title = m.StringField(required=True, unique=True)
    titleURL = m.StringField(required=True)
    body = m.StringField(required=True)
    date = m.DateField(default=datetime.datetime.utcnow)
    views = m.IntField(default=1)
    tags = m.ListField()