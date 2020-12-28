from django import forms

from .models import Memory
from .widgets import GoogleMapsAddressWidget


class MemoryForm(forms.ModelForm):
    class Meta(object):
        model = Memory
        fields = ['place_name', 'text', 'address', 'geolocation']
        widgets = {
            'address': GoogleMapsAddressWidget,
        }
