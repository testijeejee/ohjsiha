from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from .models import Note
from .forms import RegisterationForm, NoteForm, ModifyNoteForm

import json

def index(request):
    return render(request, "polls/home.html")

def register(request):
    if request.method=="POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = RegisterationForm()
    args = {'form': form}
    return render(request, "polls/register.html", args)

def loggedout(request):
    return render(request, 'polls/loggedout.html', {})

def weather(request):
    API_KEY = "8d99e4d64c439c2ba2d97e4cb53325b8"
    args = {
        "api_key": API_KEY
    }
    return render(request, 'polls/weather.html', args)

def weatherhandle(request):
    data = json.loads(request.body)
    #Change temperature from Kelvin to Celsius
    temp = data.get("main").get("temp") - 273.15
    return HttpResponse(temp)

def notes(request):
    if request.method=="POST":
        form = NoteForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('notes')

    form = NoteForm(user=request.user)

    args = { 'form': form }

    return render(request, 'polls/notes.html', args)

def modifyNote(request, noteId):
    try:
        if request.method=="POST":
            form = ModifyNoteForm(request.POST, instance=Note.objects.get(id=noteId))
            if form.is_valid():
                form.save()
                return redirect('notes')

        form = ModifyNoteForm(instance=Note.objects.get(id=noteId))

        args = {'form': form, 'note': Note.objects.get(id=noteId)}

        return render(request, 'polls/modify_note.html', args)

    except Note.DoesNotExist:
        return HttpResponse("Ei löydy")


def deleteNote(request, noteId):
    note = Note.objects.get(id=noteId)
    note.delete()

    return redirect('notes')
