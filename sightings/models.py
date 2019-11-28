from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model):
    latitude = models.FloatField()

    longitude = models.FloatField()

    unique_squirrel_id = models.CharField(
            help_text=_('Unique Squirrel ID'),
            max_length = 50
            )
    
    PM = 'PM'
    AM = 'AM'

    SHIFT_CHOICES = {
            (PM, 'PM'),
            (AM, 'AM'),
            }

    shift = models.CharField(
            help_text=_('shift'),
            max_length=10,
            choices=SHIFT_CHOICES,
            default=AM,
            )

    date = models.DateField(
            help_text=_('Date'),
            )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    
    AGE_CHOICES = {
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            }

    age = models.CharField(
            help_text=_('Age'),
            max_length=20,
            choices=AGE_CHOICES,
            default=ADULT,
            )
    
    GREY = 'Grey'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    COLOR_CHOICES = {
            (GREY,'Grey'),
            (CINNAMON, 'Cinnamon'),
            (BLACK, 'Black'),
            }

    primary_flur_color = models.CharField(
            help_text=_('Primary flur color'),
            max_length=30,
            choices=COLOR_CHOICES,
            default=GREY,
            )
    
    ABOVE_GROUND = 'Above Ground'
    GROUND_PLANE = 'Ground Plane'

    LOCATION_CHOICES = {
            (ABOVE_GROUND, 'Above Ground'),
            (GROUND_PLANE, 'Ground Plane'),
            }

    location = models.CharField(
            help_text=_('location'),
            max_length=50,
            choices=LOCATION_CHOICES,
            default=ABOVE_GROUND,
            )

    specific_location = models.CharField(
            help_text=_('Specific location'),
            max_length=100
            )

    running = models.BooleanField(
            help_text=_('Squirrel was seen running'),
            )

    chasing = models.BooleanField(
            help_text=_('Squirrel was seen chasing another squirrel')
            )

    climbing = models.BooleanField(
            help_text=_('Squirrel was seen climbing'),
            )

    eating = models.BooleanField(
            help_text=_('Squirrel was seen eating'),
            )

    foraging = models.BooleanField(
            help_text=_('Squirrel was seen foraging for food'),
            )

    other_activities = models.CharField(
            help_text=_('Other activities'),
            max_length = 100
            )

    kuks = models.BooleanField(
            help_text=_('Squirrel was heard kukking'),
            )

    quaas = models.BooleanField(
            help_text=('Squirrel was heard quaaing'),
            )

    moans = models.BooleanField(
            help_text=_('Squirrel was heard moaning'),
            )

    tail_flags = models.BooleanField(
            help_text=_('Squirrel was seen flagging its tail'),
            )

    tail_twitches =  models.BooleanField(
            help_text=_('Squirrel was seeen twitching its tail'),
            )

    approaches = models.BooleanField(
            help_text=_('Squirrel was seen approaching human, seeking food'),
            )

    indifferent = models.BooleanField(
            help_text=_('Squirrel was indifferent to human presence'),
            )

    runs_from = models.BooleanField(
            help_text=_('Squirrel was seen running from humans'),
            )

    def __str__(self):
        return self.unique_squirrel_id
