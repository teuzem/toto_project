from django import forms
from .models import Record

# Formulaire pour créer ou mettre à jour un enregistrement
class RecordForm(forms.ModelForm):
    class Meta:
        model = Record  # Utilise le modèle Record
        fields = ['title', 'description']  # Champs à inclure dans le formulaire