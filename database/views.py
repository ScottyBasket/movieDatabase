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
from django.db.models import Q
from django.views.generic import TemplateView, ListView

import random

templates = "static/css/style.css"


class IndexView(ListView):
    template_name = 'index.html'
    model = Movie

    def get(self, request):
        movies = Movie.objects.all().order_by("name")
        context = {
            'movies': movies,
        }
        return render(request, self.template_name, context)


class SearchResultsView(ListView):
    model = Movie
    template_name = 'results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Movie.objects.filter(
            Q(name__icontains=query) | Q(
                genre__icontains=query) | Q(barcode__icontains=query) | Q(rating__icontains=query) | Q(name2__icontains=query)
        )
        return object_list


class Landing(View):
    template_name = 'landing.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


def index(request):
    data = Image.objects.all()
    context = {
        'data': data
    }
    return render(request, "display.html", context)
