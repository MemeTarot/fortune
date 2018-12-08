from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
from .forms import SpreadForm
from .models import MajorArcanaCard, Placement
from random import sample


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = SpreadForm(request.GET)
    else:
        form = SpreadForm()

    return render(request, 'reader/home.html', {'form': form})


def readings(request):
    cards = MajorArcanaCard.objects.all()
    for card in cards:
        card.url = url = static(card.imgUrl)

    spread_pk = int(request.POST.get('spread'))
    placements = [place for place in Placement.objects.all() if place.spread.pk == spread_pk]
    random_cards = choose_items(cards, 3)
    reading = zip(placements, random_cards)

    return render(request, 'reader/readings.html', {'reading': reading})


def choose_items(collection, n):
    """Returns a list of <n> random items from <collection>."""
    rand_indexes = sample(range(0, len(collection)), n)
    return [collection[index] for index in rand_indexes]
