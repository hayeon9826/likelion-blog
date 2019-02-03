from django import forms
from .models import Portfolio

class PotfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('author', 'title', 'image', 'category', 'discription')