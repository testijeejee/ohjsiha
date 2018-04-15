from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Question

def index(request):
    import datetime

    question = Question()
    question.question_text = "Moi"
    question.pub_date = datetime.datetime.now()
    question.save()
    return render(request, "polls/home.html")

def register(request):
    return render(request, "polls/register.html")
