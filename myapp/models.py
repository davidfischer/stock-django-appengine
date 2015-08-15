# To use Django models, you'd need to connect to CloudSQL and configure
# settings.DATABASES. Another alternative is to use a third-party module
# like djangae or django-nonrel (and it's requirements).
# However, if you want, you can just use Appengine models and the Appengine
# datastore and not rely on anything.
from google.appengine.ext import ndb


class Poll(ndb.Model):
    question = ndb.StringProperty(required=True)
    publish_date = ndb.DateTimeProperty(auto_now_add=True)

    def __unicode__(self):
        return self.question


class Choice(ndb.Model):
    poll = ndb.KeyProperty(kind=Poll, required=True)
    choice = ndb.StringProperty()
    votes = ndb.IntegerProperty()
