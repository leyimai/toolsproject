from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sighting
import csv
import datetime

class Command(BaseCommand):
    help = 'Importing the squirrel data into databse according the file path specifiede.'
    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="file path")

    def handle(self, *args, **options):
        #if len(args) != 1:
           # raise CommandError("Only 1 argument is allowed")
        #path = args[0]
        path = options['path']
        with open(path,'r') as fp:
            rows = list(csv.DictReader(fp))
            row = dict(rows[0]).values()
        def change_format(row):
            for i in range(len(row)):
                row[i] = str(row[i]).strip()
                if row[i] in ['TRUE', 'true']:
                    row[i] = True
                if row[i] in ['FALSE', 'false']:
                    row[i] = False
            return row

        for i in range(len(rows[:5])):
            try:
                row_raw = list(dict(rows[i]).values())
                row = change_format(row_raw)
                s = Sighting(latitude=float(row[0]), longitude=float(row[1]),
                     unique_squirrel_id=str(row[2]), shift = row[4],
                     date = datetime.datetime.strptime(str(row[5]),'%m%d%Y').date(), 
                     age = row[7], primary_flur_color = row[8],
                     location = row[12], specific_location = row[14],
                    running = row[15], chasing = row[16], climbing = row[17], eating = row[18],
                    foraging = row[19],other_activities = row[20], kuks = row[21], quaas = row[22],
                    moans = row[23], tail_flags = row[24], tail_twitches = row[25], approaches = row[26], 
                    indifferent = row[27], runs_from = row[28],
                    )
                print(s)
            except Exception as e:
                raise CommandError(e)
        self.stdout.write(self.style.SUCCESS('Successfully import squirrel data'))
