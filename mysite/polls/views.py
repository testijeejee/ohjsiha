from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse


from .models import Question
from .forms import RegisterationForm

def index(request):
    import datetime

    question = Question()
    question.question_text = "Moi"
    question.pub_date = datetime.datetime.now()
    question.save()
    return render(request, "polls/home.html")

def register(request):
    if request.method=="POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    form = RegisterationForm()
    args = {'form': form}
    return render(request, "polls/register.html", args)

def loggedout(request):
    return render(request, 'polls/loggedout.html', {})
