from django.forms.models import ModelForm
from .models import Temas

class TemasForm(ModelForm):
    class Meta:
        model = Temas
        fields = '__all__'