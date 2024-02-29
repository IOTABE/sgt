from django import forms
from .models import Motorista, Veiculo, Setores


class MotoristaForm(forms.ModelForm):

    class Meta:
        model = Motorista
        fields = "__all__"


class  VeiculoForm(forms.ModelForm):

    class Meta:
        model = Veiculo
        fields = "__all__"


class  SetorForm(forms.ModelForm):

    class Meta:
        model = Setores
        fields = "__all__"