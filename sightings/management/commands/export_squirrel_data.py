from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sighting
import csv
import datetime
import pandas as pd

class Command(BaseCommand):
    help = 'Exporting the squirrel data'
    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="file path")

    def handle(self, *args, **options):
        sightings = Sighting.objects.all()
        output_list = list()
        for sighting in sightings:
            dic = dict()
            dic['latitude'] = sighting.latitude
            dic['longitude'] = sighting.longitude
            dic['unique_squirrel_id'] = sighting.unique_squirrel_id
            dic['shift'] = sighting.shift
            dic['date'] = sighting.date.strftime('%m%d%Y')
            dic['age'] = sighting.age
            dic['primary_flur_color'] = sighting.primary_flur_color
            dic['location'] = sighting.location
            dic['specific_location'] = sighting.specific_location
            dic['running'] = sighting.running
            dic['chasing'] = sighting.chasing
            dic['climbing'] = sighting.climbing
            dic['eating'] = sighting.eating
            dic['foraging'] = sighting.foraging
            dic['other_activities'] = sighting.other_activities
            dic['kuks'] = sighting.kuks
            dic['quaas'] = sighting.quaas
            dic['moans'] = sighting.moans
            dic['tail_flags'] = sighting.tail_flags
            dic['tail_twitches'] = sighting.tail_twitches
            dic['approaches'] = sighting.approaches
            dic['indifferent'] = sighting.indifferent
            dic['runs_from'] = sighting.runs_from
            output_list.append(dic)
        output_df = pd.DataFrame(output_list)
        output_df.to_csv(path)
        self.stdout.write(self.style.SUCCESS('Successfully export squirrel data'))
