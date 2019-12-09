from django.shortcuts import render
from sightings.models import Sighting

def map(request):
    sightings = Sighting.objects.all()[:60]
    context = {
            'sightings': sightings,
            }

    return render(request, 'map/map.html', context)
