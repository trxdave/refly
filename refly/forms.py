from django import forms
from .models import CheatSheet

class CheatSheetForm(forms.ModelForm):
    class Meta:
        model = CheatSheet
        fields = ['title', 'category', 'content']