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
    name = models.CharField('Name', max_length=255, unique=False, blank=False)
    barcode = models.IntegerField(
        'Barcode', null=True)
    year = models.DateField('Date', null=True)
    genre = models.CharField('Genre', max_length=255, null=True)
    rating = models.IntegerField('Rating', null=True)
    runTime = models.IntegerField('Run Time', null=True)
    director = models.CharField('Director', max_length=255, null=True)
    description = models.CharField('Description', max_length=255, null=True)

    def __str__(self):
        return self.name
