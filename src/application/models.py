from google.appengine.ext import ndb


class BoiledModel(ndb.Model):
    boiled_name = ndb.StringProperty(required=True)

