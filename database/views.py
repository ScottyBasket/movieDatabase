from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse_lazy, reverse
from django.views.generic import View
from django.utils.safestring import mark_safe  # to add blank line in forms
from django.utils.translation import gettext, gettext_lazy as _
from .models import Movie

import random


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        movies = Movie.objects.all()
        context = {
            'movies': movies,
        }
        return render(request, self.template_name, context)


def index(request):
    data = Image.objects.all()
    context = {
        'data': data
    }
    return render(request, "display.html", context)
