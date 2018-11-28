from django.shortcuts import render
from .models import MajorArcanaCard
from random import sample


# Create your views here.
def home(request):
    return render(request, 'reader/home.html')


def readings(request):
    cards = MajorArcanaCard.objects.order_by('number')
    num_cards = int(request.POST.get('spread'))
    print(num_cards)
    spread = choose_items(cards, num_cards)
    return render(request, 'reader/readings.html', {'spread': spread})


def choose_items(collection, n):
    """Returns a list of <n> random items from <collection>."""
    rand_indexes = sample(range(0, len(collection)), n)
    return [collection[index] for index in rand_indexes]
