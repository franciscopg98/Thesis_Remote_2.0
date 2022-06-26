from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PolygonField
import basic_app.models
import datetime


class Query(basic_app.models.Query):
    
    POLARIZATION_CHOICES = (
    ("HH", "HH"),
    ("VV", "VV"),
    ("HV", "HV"),
    ("VH", "VH"),
    ("HH HV", "HH HV"),
    ("VV VH", "VV VH"),
    )

    SWATH_IDENTIFIER_CHOICES = (

    ("S1", "S1"),
    ("S2", "S2"),
    ("S3", "S3"),
    ("S4", "S4"),
    ("S5", "S5"),
    ("S6", "S6"),
    ("IW", "IW"),
    ("IW1", "IW1"),
    ("IW2", "IW2"),
    ("IW3", "IW3"),
    ("EW", "EW"),
    ("EW1", "EW1"),
    ("EW2", "EW2"),
    ("EW3", "EW3"),
    ("EW4", "EW4"),
    ("EW5", "EW5"),
    )

    SENSOR_MODE_CHOICES = (
    ("SM", "SM"),
    ("IW", "IW"),
    ("EW", "EW"),
    ("WV", "WV"),
    )

    ORBIT_DIRECTION_CHOICES = (
    ("Ascending", "Ascending"),
    ("Descending", "Descending"),
    )

    TIMELINESS_CHOICES = (
    ("NRT", "NRT-3h"),
    ("NTC", "Fast-24h"),
    )
    
    ingestiondate = models.DateTimeField(default = datetime.datetime.now())

    orbitnumber = models.IntegerField(null=True)

    lastorbitnumber = models.IntegerField(null=True)

    relativeorbitnumber = models.IntegerField(null=True)

    lastrelativeorbitnumber = models.IntegerField(null=True)

    orbitdirection = models.CharField(max_length=25,
                  choices=ORBIT_DIRECTION_CHOICES,
                  default="Ascending")

    timeliness = models.CharField(max_length=25,
                  choices=TIMELINESS_CHOICES,
                  default="Ascending")
   
    polarization = models.CharField(max_length=15,
                  choices=POLARIZATION_CHOICES,
                  default="HH")
 
   
    swath_identifier = models.CharField(max_length=15,
                  choices=SWATH_IDENTIFIER_CHOICES,
                  default="S1")

    
    sensor_operational_mode = models.CharField(max_length=15,
                  choices=SENSOR_MODE_CHOICES,
                  default="SM")

    tag = models.OneToOneField(basic_app.models.Query, parent_link=True,on_delete=models.CASCADE, default = '1', related_name="%(app_label)s_%(class)s_related")
    
    class Meta:
        app_label = 'S_1'
        

    