from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model= Tarea
        fields = ['titulo','descripcion', 'estado','label']
        
class FiltroTareaForm(forms.Form):
    estado = forms.ChoiceField(choices=[('','--------')] + Tarea.ESTADO_CHOICES, required=False)
    etiqueta = forms.ChoiceField(choices=[('','--------')] + Tarea.LABEL_CHOICES, required=False)
        
"""    def __init__(self, *args, **kwargs):
        super(Tareaform, self).__init__(*args, **kwargs)

        form_fields = ['titulo', 'descripcion']
        for field in form_fields:
            self.fields[field].widget.attrs['class'] = 'form-control'"""

