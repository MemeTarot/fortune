from django import forms
from .models import Spread


class SpreadForm(forms.Form):
    SPREAD_CHOICES = [(spread, spread.title) for spread in Spread.objects.all()]

    spread = forms.CharField(label='Choose a spread',
                             widget=forms.Select(choices=SPREAD_CHOICES))
