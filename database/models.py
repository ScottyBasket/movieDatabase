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
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name
