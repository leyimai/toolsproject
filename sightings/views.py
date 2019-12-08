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
    template = loader.get_template('sightings/stats.html')
    total_number = Sighting.objects.all().count()
    pm_shift = Sighting.objects.filter(shift='PM').count()
    am_shift = Sighting.objects.filter(shift='AM').count()
    num_of_adults = Sighting.objects.filter(age='Adult').count()
    num_of_juveniles = Sighting.objects.filter(age='Juvenile').count()
    num_of_climbing = Sighting.objects.filter(climbing = True).count()
    context = {
            'total_number': total_number,
            'pm_shift': pm_shift,
            'am_shift': am_shift,
            'num_of_adults': num_of_adults,
            'num_of_juveniles':num_of_juveniles,
            'num_of_climbing': num_of_climbing,
            }
    return HttpResponse(template.render(context, request))

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


