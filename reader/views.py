from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
from .forms import SpreadForm
from .models import MajorArcanaCard, Placement
from random import sample


# Create your views here.

def home(request):
    """The Home Page view"""
    if request.method == 'POST':
        form = SpreadForm(request.GET)
    else:
        form = SpreadForm()

    return render(request, 'reader/home.html', {'form': form})


def readings(request):
    """The Readings Page view"""
    cards = MajorArcanaCard.objects.all()
    for card in cards:
        card.url = static(card.imgUrl)

    # Receives the spread chosen by the user
    spread_pk = int(request.POST.get('spread'))
    # Returns a list of placements for the chosen spread
    placements = [place for place in Placement.objects.all() if place.spread.pk == spread_pk]
    # Choose three random cards from the tarot deck
    random_cards = choose_items(cards, 3)
    # (placement, card) list
    reading = zip(placements, random_cards)

    return render(request, 'reader/readings.html', {'reading': reading})


def choose_items(collection, n):
    """Returns a list of <n> random items from <collection>."""
    rand_indexes = sample(range(0, len(collection)), n)
    return [collection[index] for index in rand_indexes]
