from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate

# Create your views here.
def index(resquest):
    candidates = Candidate.objects.all()

    return render(resquest, 'elections/index.html')
