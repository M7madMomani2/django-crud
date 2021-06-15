from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from .models import Snack

# Create your views here.
class SnackListView (TemplateView):
    pass
class SnackDetailView (TemplateView):
    pass
class SnackCreateView (TemplateView):
    pass
class SnackUpdateView  (TemplateView):
    pass
class SnackDeleteView (TemplateView):
    pass
