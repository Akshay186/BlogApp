from django.template import Library
register = Library()

@register.filter
def get_count(post):
    return post.count()