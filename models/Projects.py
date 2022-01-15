import mongoengine as m

class Projects(m.Document):
    title= m.StringField(required=True, unique=True)
    titleURL = m.StringField(reqiured=True)
    miniText = m.StringField(required=True)
    technologies = m.StringField(required=True)
