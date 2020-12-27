from .models import Memory
from django import forms
from .widgets import GoogleMapsAddressWidget


class MemoryForm(forms.ModelForm):
    class Meta(object):
        model = Memory
        fields = ['address', 'geolocation', 'place_name', 'text']
        widgets = {
            "address": GoogleMapsAddressWidget,
        }
