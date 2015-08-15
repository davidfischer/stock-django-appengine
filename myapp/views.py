from django.shortcuts import render_to_response
from django.http import Http404

from myapp.models import Poll, Choice


def home(request):
    #request.session['greeting'] = 'Hello yourname'
    greeting = request.session.get('greeting', 'Hello Appengine')
    return render_to_response('home.html', {'greeting': greeting})


def polls(request):
    poll_list = Poll.query().order(Poll.question)
    return render_to_response('polls.html', {'polls': poll_list})


def poll(request, poll_id):
    # This 3 line combination could use a shortcut like get_object_or_404
    p = Poll.get_by_id(int(poll_id))
    if p is None:
        raise Http404

    choices = Choice.query(Choice.poll == p.key).fetch()

    return render_to_response(
        'poll.html',
        {
            'poll': p,
            'choices': choices,
        }
    )
