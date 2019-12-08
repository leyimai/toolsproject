from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sighting
import csv
import datetime

class Command(BaseCommand):
    help = 'Importing the squirrel data into databse according the file path specifiede.'
    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="file path")

    def handle(self, *args, **options):
        path = options['path']
        with open(path,'r') as fp:
            rows = list(csv.DictReader(fp))

        def change_format(row):
            for key in row.keys():
                row[key] = str(row[key]).strip()
                if row[key] in ['TRUE', 'true']:
                    row[key] = True
                if row[key] in ['FALSE', 'false']:
                    row[key] = False
            return row

        for row in rows:
            try:
                row = change_format(row)
                s = Sighting(latitude = float(row['latitude']), 
                    longitude = float(row['longitude']),
                    unique_squirrel_id = str(row['unique_squirrel_id']), 
                    shift =  row['shift'],
                    date = datetime.datetime.strptime(str(row['date']),'%m%d%Y').date(), 
                    age = row['age'], 
                    primary_flur_color = row['primary_flur_color'],
                    location = row['location'], 
                    specific_location = row['specific_location'],
                    running = row['running'], 
                    chasing = row['chasing'], 
                    climbing = row['climbing'], 
                    eating = row['eating'],
                    foraging = row['foraging'],
                    other_activities = row['other_activities'], 
                    kuks = row['kuks'], 
                    quaas = row['quaas'],
                    moans = row['moans'], 
                    tail_flags = row['tail_flags'], 
                    tail_twitches = row['tail_twitches'], 
                    approaches = row['approaches'], 
                    indifferent = row['indifferent'], 
                    runs_from = row['runs_from'],
                s.save()
            except Exception as e:
                raise CommandError(e)
        self.stdout.write(self.style.SUCCESS('Successfully import squirrel data'))
