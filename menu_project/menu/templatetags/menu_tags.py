from django import template
from menu.models import Menu

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.prefetch_related('items__children').get(name=menu_name)
        request = context['request']
        current_url = request.path
        return {
            'menu': menu,
            'current_url': current_url,
        }
    except Menu.DoesNotExist:
        return {
            'menu': None,
            'current_url': None,
        }
