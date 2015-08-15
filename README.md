# Stock Django on Appengine

This is a fairly simple Django project that illustrates how to create a Django
project that runs on Google Appengine.

This project relies on a version of Django (1.4 for now) bundled with
Appengine as opposed to a forked version of Django specific to Appengine.
For more details, see the [Appengine Django notes][appengine-django].

[appengine-django]: https://cloud.google.com/appengine/docs/python/tools/libraries27#django


This project does not use CloudSQL (Google's relational database) which
is necessary for using Django models and Django's ORM, models and admin
interface. Instead it uses Appengine models that store to the non-relational
datastore. This allows using Appengine models where non-relational data
is best and CloudSQL where relational data is best.
