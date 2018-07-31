from django.shortcuts import render

from minerals.models import Mineral


def home(request):
    return render(request, 'home.html')
