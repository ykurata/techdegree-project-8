from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Mineral
import string


alphabet = string.ascii_uppercase


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html',
            {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_detail.html',
            {'mineral': mineral})


def search(request):
    term = request.GET.get('q')
    minerals = Mineral.objects.filter(name__icontains=term)
    return render(request, 'minerals/mineral_list.html',
            {'minerals': minerals})


def first_letter(request):
    mineral = Mineral.objects.filter(name__startswith=alphabet)
    return render(request, 'minerals/mineral_list.html',
            {'minerals': minerals, 'alphabet': alphabet})
