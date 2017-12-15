from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate, Poll, Choice
import datetime as dt

# Create your views here.
def index(resquest):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}
    return render(resquest, 'elections/index.html', context)

def areas(resquest, area):
    today = dt.datetime.now()
    try:
        poll = Poll.objects.get(area = area, start_date__lte = today, end_date__gte = today)
        candidates = Candidate.objects.filter(area = area)

    except:
        poll = None
        candidates = None
    context = {'candidates' : candidates,
     'area' : area,
     'poll' : poll}
    return render(resquest, 'elections/area.html', context)
