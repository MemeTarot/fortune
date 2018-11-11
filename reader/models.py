from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    meaning = models.TextField()
    imgUrl = models.TextField()

    def __str__(self):
        return self.title
