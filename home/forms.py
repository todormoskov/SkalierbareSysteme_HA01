from django.forms import ModelForm
from .models import Aufgaben

class TODOForm(ModelForm):
    class Meta:
        model = Aufgaben
        fields = ['aufgabe', 'deadline', 'status']
