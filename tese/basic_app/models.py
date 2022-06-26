from django.db import models
from django.contrib.auth.models import User
import jsonfield
from djgeojson.fields import PolygonField
from django.contrib.contenttypes.models import ContentType
import datetime

# Create your models here.
#class User(models.Model):

    #user=models.OneToOneField(User, on_delete=models.PROTECT)

   # def __str__(self):
       # return self.user.username

class Platform(models.Model):
    id = models.IntegerField()
    slug = models.CharField(max_length=30,primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000, default="Description")
    user_guide_url = models.CharField(max_length=1000)
    tech_guide_url = models.CharField(max_length=1000)
    #url = jsonfield.JSONField()
    def __str__(self):
        return self.slug
    
    class Meta:
        app_label  = 'basic_app'
    

class Product(models.Model):
    id = models.IntegerField()
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    slug = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=100)
    product_level = models.CharField(max_length=30)
    description = models.CharField(max_length=1000, default="Description")
    url = models.CharField(max_length=1000)
    def __str__(self):
        return self.slug
    
    class Meta:
        app_label  = 'basic_app'


class Query(models.Model):

    id = models.AutoField(primary_key=True)
    
    user =  models.ForeignKey(User,null=True, on_delete=models.PROTECT)
    
    platform = models.CharField(max_length=20,default="platform")

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    descrip = models.TextField(max_length=1000, default="This Query is relative to ...")

    startdate = models.DateTimeField(default = datetime.datetime.now())

    enddate = models.DateTimeField(default = datetime.datetime.now())

    area = PolygonField(null=True)

    class Meta:
        app_label = 'basic_app'

    

    

    
   

#class Results(models.Model):
