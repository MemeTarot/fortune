from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Generic information shared by both arcanas
class Card(models.Model):
    description = models.TextField()
    meaning = models.TextField()
    imgUrl = models.URLField()
    altText = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class MajorArcanaCard(Card):
    number = models.IntegerField(validators=[MaxValueValidator(22), MinValueValidator(0)])
    title = models.CharField(max_length=200)


# Major arcana cards, select from list of suits and faces
class MinorArcanaCard(Card):
    SWORDS = 'SW'
    CUPS = 'CP'
    WANDS = 'WD'
    PENTACLES = 'PT'
    SUITS_CHOICES = (
        (SWORDS, 'Swords'),
        (CUPS, 'Cups'),
        (WANDS, 'Wands'),
        (PENTACLES, 'Pentacles'),
        (None, 'Select a suit')
    )
    suit = models.CharField(
        max_length=2,
        choices=SUITS_CHOICES,
        default=None
    )
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    PAGE = 'P'
    KNIGHT = 'N'
    QUEEN = 'Q'
    KING = 'K'
    FACE_CHOICES = (
        (ONE, 'One'),
        (TWO, 'Two'),
        (THREE, 'Three'),
        (FOUR, 'Four'),
        (FIVE, 'Five'),
        (SIX, 'Six'),
        (SEVEN, 'Seven'),
        (EIGHT, 'Eight'),
        (NINE, 'Nine'),
        (TEN, 'Ten'),
        (PAGE, 'Page'),
        (KNIGHT, 'Knight'),
        (QUEEN, 'Queen'),
        (KING, 'King'),
        (None, 'Select a face')
    )
    face = models.CharField(
        max_length=1,
        choices=FACE_CHOICES,
        default=None
    )
