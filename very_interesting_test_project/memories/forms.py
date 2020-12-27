from .models import Memory
from django import forms


class MemoryForm(forms.ModelForm):
    class Meta(object):
        model = Memory
        fields = ['place_name', 'text']
