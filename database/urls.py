from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("search/", views.SearchResultsView.as_view(), name="results"),
    path('landing/', views.Landing.as_view(), name='landing'),
    path('', views.IndexView.as_view(), name='home'),
]
