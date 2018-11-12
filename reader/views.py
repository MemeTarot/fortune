from django.shortcuts import render
from .models import MajorArcanaCard

# Create your views here.
def card_list(request):
    cards = MajorArcanaCard.objects.all()
    return render(request, 'reader/card_list.html', {'cards': cards})

