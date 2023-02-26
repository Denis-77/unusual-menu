from django import template
from menu_app.models import Menu

register = template.Library()


@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, url: str):
    urls = url.split('/')
    category = urls[-1]
    urls.append('')
    levels = len(urls)
    menus = Menu.objects.filter(parent_url__in=urls).order_by('full_url')
    return {
        'menu_items': menus,
        'levels': range(levels),
        'category': category
    }
