from django.shortcuts import render

from minerals.models import Mineral

def home(request):
    minerals = Mineral.objects.filter(name__istartswith="A")
    return render(request, 'home.html', {'minerals': minerals})
