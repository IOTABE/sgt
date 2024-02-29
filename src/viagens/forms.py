from django import forms
from .models import Viagens



class  ViagensForm(forms.ModelForm):

    class Meta:
        model = Viagens
        fields = "__all__"