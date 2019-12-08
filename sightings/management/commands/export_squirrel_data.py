from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sighting
import csv
import datetime

class Command(BaseCommand):
    help = 'Exporting the squirrel data'
    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="file path")

    def handle(self, *args, **options):
        path = options['path']
        sightings = Sighting.objects.all()
        with open(path, 'w', newline='') as csvfile:
            sightings = Sighting.objects.all()
            fieldnames = ['latitude', 'longitude', 'unique_squirrel_id', 'shift', 'date', 'age', 
                          'primary_flur_color', 'location', 'specific_location', 'running', 'chasing', 
                          'climbing', 'eating', 'foraging', 'other_activities', 'kuks', 'quaas', 'moans', 
                          'tail_flags', 'tail_twitches', 'approaches', 'indifferent', 'runs_from']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in sightings:
                dic = dict()
                dic['latitude'] = row.latitude
                dic['longitude'] = row.longitude
                dic['unique_squirrel_id'] = row.unique_squirrel_id
                dic['shift'] = row.shift
                dic['date'] = row.date.strftime('%m%d%Y')
                dic['age'] = row.age
                dic['primary_flur_color'] = row.primary_flur_color
                dic['location'] = row.location
                dic['specific_location'] = row.specific_location
                dic['running'] = row.running
                dic['chasing'] = row.chasing
                dic['climbing'] = row.climbing
                dic['eating'] = row.eating
                dic['foraging'] = row.foraging
                dic['other_activities'] = row.other_activities
                dic['kuks'] = row.kuks
                dic['quaas'] = row.quaas
                dic['moans'] = row.moans
                dic['tail_flags'] = row.tail_flags
                dic['tail_twitches'] = row.tail_twitches
                dic['approaches'] = row.approaches
                dic['indifferent'] = row.indifferent
                dic['runs_from'] = row.runs_from
                writer.writerow(dic)
        self.stdout.write(self.style.SUCCESS('Successfully export squirrel data'))
