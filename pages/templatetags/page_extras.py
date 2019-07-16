from django import template
from pages.models import Page
import datetime

register = template.Library()

@register.simple_tag
def get_pages_list():
    pages = Page.objects.all()
    return pages


@register.simple_tag
def year():
    year = datetime.datetime.now().year
    return year