from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting
from django.template import loader

def index(request):
    
    latest_sighting_list = Sighting.objects.all()
    template = loader.get_template('sightings/index.html')
    context = {
            'latest_sighting_list': latest_sighting_list,
            }
    return HttpResponse(template.render(context, request))


def add(request):
    return HttpResponse('Hi')

def stats(request):
    return HttpResponse('Hi')

def details(request, unique_squirrel_id):
    sighting = Sighting.objects.get(unique_squirrel_id = unique_squirrel_id)
    return HttpResponse(sighting.unique_squirrel_id)


