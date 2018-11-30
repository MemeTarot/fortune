from django.shortcuts import render
from random import sample
from .models import MajorArcanaCard

# Create your views here.

def home(request):
    return render(request, 'reader/home.html')

def readings(request):
    cards = MajorArcanaCard.objects.all()
    num_cards = int(request.POST.get('spread', 0))
    spread = choose_items(cards, num_cards)
    return render(request, 'reader/readings.html', {'spread': spread})

def choose_items(collection, n):
    """Returns a list of <n> random items from <collection>."""
    rand_indexes = sample(range(0, len(collection)), n)
    return [collection[index] for index in rand_indexes]
