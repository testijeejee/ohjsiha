from django.shortcuts import render, redirect
import json
from django.core import serializers
# Create your views here.
from django.http import HttpResponse
from django.utils import timezone
from django.http import JsonResponse

from .models import Note, WeatherSearch
from .forms import RegisterationForm, NoteForm, ModifyNoteForm

import json

def index(request):
    args = {
        "searches": WeatherSearch.objects.all(),
        "searches_distinct": WeatherSearch.objects.all()
    }
    return render(request, "polls/home.html", args)

def createGraph(request, graphType):
    if graphType == "city":
        search_objects = WeatherSearch.objects.values_list("city", flat=True)
        objects = list(search_objects)


    elif graphType == "temp":
        celsius_objects = WeatherSearch.objects.values_list("celsius", flat=True)
        city_objects = WeatherSearch.objects.values_list("city", flat=True)
        search_objects = {}

        for i in range(0, len(celsius_objects)):
            if city_objects[i] in search_objects:
                search_objects[city_objects[i]].append(celsius_objects[i])
            else:
                search_objects[city_objects[i]] = [celsius_objects[i]]

        for i in search_objects:
            sum = 0
            for amount in search_objects[i]:
                sum = sum + amount

            search_objects[i] = sum/len(search_objects[i])

        objects = search_objects

    return JsonResponse(objects, safe=False)

def cityList(request, cityName):
    searches = WeatherSearch.objects.filter(city = cityName)
    objects = {}
    for i in searches:
        objects[i.pub_date.strftime('%m/%d/%Y')] = i.celsius

    return JsonResponse(objects)


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

    weathersearch = WeatherSearch()
    weathersearch.celsius = temp
    weathersearch.pub_date = timezone.now()
    weathersearch.city = data.get("name")
    weathersearch.lat = data.get("coord").get("lat")
    weathersearch.lon = data.get("coord").get("lon")
    weathersearch.save()

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
