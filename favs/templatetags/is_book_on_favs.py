from django import template
from favs.models import FavList

register = template.Library()

@register.simple_tag(takes_context=True)
def is_book_on_favs(context,book):
  user = context.request.user
  try:
    the_list = FavList.objects.get(created_by=user)
    return book in the_list.books.all()
  except FavList.DoesNotExist:
    return False