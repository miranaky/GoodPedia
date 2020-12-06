from django import template
from favs.models import FavList

register = template.Library()

@register.simple_tag(takes_context=True)
def is_movie_on_favs(context,movie):
  user = context.request.user
  try:
    the_list = FavList.objects.get(created_by=user)
    return movie in the_list.movies.all()
  except FavList.DoesNotExist:
    return False

