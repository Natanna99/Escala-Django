from django import forms
from datetime import date
from .models import *

class Cadastrar_Medico_Form(forms.Form):
    nome= forms.CharField(max_length=30, min_length=4)
    sobrenome= forms.CharField(max_length= 150, min_length=5)
    data_admissao= forms.DateField(initial=date)

    def clean(self):
        dados = super().clean()
        return dados

class Cadastrar_Posto_Form(forms.Form):
    nome= forms.CharField(max_length=30, min_length=4)
    endereco= forms.CharField(max_length= 150)
    
    def clean(self):
        dados = super().clean()
        return dados

class Cadastrar_Folga_Form(forms.Form):
    dia= forms.DateField()
    medico= forms.ModelChoiceField(queryset= Medico.objects.all())
    
    def clean(self):
        dados = super().clean()
        return dados

class Cadastrar_Escala_Form(forms.Form):
    medico= forms.ModelChoiceField(queryset= Medico.objects.all())
    folga= forms.ModelChoiceField(queryset= Folga.objects.all())
    posto= forms.ModelChoiceField(queryset= Posto.objects.all())
    data= forms.DateField()
    
    def clean(self):
        dados = super().clean()
        return dados