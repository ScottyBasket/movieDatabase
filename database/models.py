import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from operator import itemgetter

MAX_NAME_LEN = 64


class Movie(models.Model):
    name = models.CharField('name', max_length=255, unique=False, blank=False)
    name2 = models.CharField('name2', max_length=255, blank=True)
    barcode = models.IntegerField(
        'Barcode', null=True)
    year = models.IntegerField(
        'Year', blank=True)
    genre = models.CharField('Genre', max_length=255, null=True)
    rating = models.CharField('Rating', null=True, max_length=5)
    score = models.IntegerField('Score', null=True)
    runTime = models.IntegerField('Run Time', null=True)
    director = models.CharField('Director', max_length=255, null=True)
    description = models.CharField('Description', max_length=255, null=True)

    def __str__(self):
        return self.name    
    
    def getCount(self):
        count = len(Movie)
        return self.count