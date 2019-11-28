from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sighting
import csv

class Command(BaseCommand):
    help = 'Import the csv of squirrel data into sighting database.'

    def handle(self, *args, **options):
        
        with open(args[0], 'r') as file:
            rows = csv.reader(file, delimiter=",")

            for row in rows:

               row[0]
