# Adapted from http://blog.neutrondrive.com/posts/238134-django-on-gae-memcache
# and django/core/cache/backends/memcached.py (Django 1.4)
from django.core.cache.backends.memcached import BaseMemcachedCache


class AppengineMemcached(BaseMemcachedCache):
    def __init__(self, server, params):
        from google.appengine.api import memcache
        super(AppengineMemcached, self).__init__(
            server,
            params,
            library=memcache,
            value_not_found_exception=ValueError
        )
