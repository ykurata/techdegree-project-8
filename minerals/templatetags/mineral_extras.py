from django import template

from minerals.models import Mineral

register = template.Library()


@register.inclusion_tag('minerals/group_list.html')
def group_list(selected_group):
    groups = Mineral.objects.values_list('group', flat=True).distinct()
    return {'groups' : groups, 'selected_group': selected_group}


@register.inclusion_tag('minerals/color_list.html')
def color_list(selected_color):
    colors = Mineral.objects.values_list('color', flat=True).distinct()
    return {'colors': colors, 'selected_color': selected_color}
