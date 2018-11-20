from ..models import Article,Category,Tag
from django import template
register = template.Library()

@register.simple_tag
def get_recent_article(num=5):
    return Article.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return Article.objects.dates("created_time","month",order="DESC")

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_tags():
    return Tag.objects.all()
    