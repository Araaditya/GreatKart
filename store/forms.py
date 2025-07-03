from django import forms
from .models import RevieRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = RevieRating
        fields = ['subject','review','rating']