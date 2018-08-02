from django.db.models import Max
from django.shortcuts import get_object_or_404, render

from .models import Mineral
import string
import random


def mineral_list(request):
    """Show a list of all minerals"""
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html',
        {'minerals': minerals})


def mineral_detail(request, pk):
    """Show a mineral detail"""
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_detail.html',
        {'mineral': mineral})


def random_mineral(request):
    """Show a random mineral"""
    max_id = Mineral.objects.aggregate(max_id=Max('id'))['max_id']
    pk = random.randint(1, max_id)
    mineral = Mineral.objects.get(pk=pk)
    return render(request, 'minerals/mineral_detail.html',
        {'mineral': mineral})


def search(request):
    """Show minerals which contains term"""
    term = request.GET.get('q')
    minerals = Mineral.objects.filter(name__icontains=term)
    return render(request, 'minerals/mineral_list.html',
        {'minerals': minerals})


def search_by_letter(request, letter):
    """Show minerals which start from a letter you selected"""
    minerals = Mineral.objects.filter(name__istartswith=letter)
    return render(request, 'minerals/mineral_list.html', {
        'minerals': minerals,
        'letter': letter
    })


def search_by_group(request, group):
    """Show minerals which are in a group you selected"""
    minerals = Mineral.objects.filter(group__icontains=group)
    return render(request, 'minerals/mineral_list.html',{
        'minerals': minerals,
        'selected_group': group
    })
