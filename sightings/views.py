from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting
from django.template import loader
from django.shortcuts import redirect
from .forms import SightingForm

def index(request):
    
    latest_sighting_list = Sighting.objects.all()
    template = loader.get_template('sightings/index.html')
    context = {
            'latest_sighting_list': latest_sighting_list,
            }
    return HttpResponse(template.render(context, request))


def add(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightingForm()
    context = {
            'form': form,
            }
    return render(request, 'sightings/details.html', context)

def stats(request):
    return HttpResponse('Hi')

def details(request, unique_squirrel_id):
    sighting = Sighting.objects.get(unique_squirrel_id = unique_squirrel_id)
    if request.method == 'POST':
        form = SightingForm(request.POST, instance = sighting)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightingForm(instance=sighting)
    context = {
            'form': form,
            }
    return render(request, 'sightings/details.html', context)


