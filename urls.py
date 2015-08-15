from django.conf.urls import patterns, url


urlpatterns = patterns(
    'myapp',
    url(r'^$', 'views.home', name='home'),
    url(r'^polls/$', 'views.polls', name='polls'),
    url(r'^poll/(?P<poll_id>\d+)/$', 'views.poll', name='poll'),
)
