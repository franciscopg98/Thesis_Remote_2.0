from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PolygonField
from django.core.validators import MaxValueValidator, MinValueValidator
import basic_app.models 
import datetime


class Query(basic_app.models.Query):
    
    ORBIT_DIRECTION_CHOICES = (
    ("Ascending", "Ascending"),
    ("Descending", "Descending"),
    )

    ingestiondate = models.DateTimeField(default = datetime.datetime.now())

    orbitnumber = models.IntegerField(null=True)

    lastorbitnumber = models.IntegerField(null=True)

    relativeorbitnumber = models.IntegerField(null=True)

    lastrelativeorbitnumber = models.IntegerField(null=True)

    orbitdirection = models.CharField(max_length=25,
                  choices=ORBIT_DIRECTION_CHOICES,
                  default="Ascending")
    
    cloud_coverage = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
     )

    tag = models.OneToOneField(basic_app.models.Query, parent_link=True,on_delete=models.CASCADE, default = '1', related_name="%(app_label)s_%(class)s_related")
    
    class Meta:
        app_label = 'S_2'
        

    