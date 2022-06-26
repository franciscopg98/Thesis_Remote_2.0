from django import forms
from django.contrib.auth.models import User
import S_1.models 
import S_2.models 
import S_5P.models 
from leaflet.forms.fields import PolygonField
from leaflet.forms.widgets import LeafletWidget


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class S1QueryForm(forms.ModelForm):
    class Meta:
         model = S_1.models.Query
         fields = ('startdate','enddate','ingestiondate','orbitnumber','lastorbitnumber','relativeorbitnumber','lastrelativeorbitnumber','orbitdirection', 'area','timeliness','polarization','swath_identifier','sensor_operational_mode')
         widgets = {'area' : LeafletWidget()}

class S2QueryForm(forms.ModelForm):
    class Meta:
         model = S_2.models.Query
         fields = ('startdate','enddate','ingestiondate','orbitnumber','lastorbitnumber','relativeorbitnumber','lastrelativeorbitnumber','orbitdirection', 'area','cloud_coverage')
         widgets = {'area' : LeafletWidget()}

class S5PQueryForm(forms.ModelForm):
    class Meta:
         model = S_5P.models.Query
         fields = ('startdate','enddate','ingestiondate','orbitnumber','lastorbitnumber','relativeorbitnumber','lastrelativeorbitnumber','orbitdirection', 'area')
         widgets = {'area' : LeafletWidget()}

           

    

