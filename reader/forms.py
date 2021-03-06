from django import forms
from django.db.utils import OperationalError
from .models import Spread


class SpreadForm(forms.Form):
    try:
        SPREAD_CHOICES = [(spread.pk, spread.title) for spread in Spread.objects.all()]

        spread = forms.CharField(label='Choose a spread',
                                 widget=forms.Select(choices=SPREAD_CHOICES))
    except OperationalError:
        pass
