from django.shortcuts import redirect,reverse
from django.views.generic import TemplateView
from movies.models import Movie
from books.models import Book
from .models import FavList

def toggle_favs(request,pk):
  fav_type=request.GET.get("type",None)
  action = request.GET.get("action",None)
  if fav_type is not None and action is not None:
    if fav_type == "movie":
      try:
        movie = Movie.objects.get(pk=pk)
        fav_list,_ = FavList.objects.get_or_create(created_by=request.user)
        if action == "add":
          fav_list.movies.add(movie)
        elif action == "remove":
          fav_list.movies.remove(movie)
        return redirect(reverse("movies:movie",kwargs={"pk":pk}))
      except Movie.DoesNotExist:
        return redirect(reverse("core:home"))
    elif fav_type == "book":
      try:
        book = Book.objects.get(pk=pk)
        fav_list,_ = FavList.objects.get_or_create(created_by=request.user)
        if action == "add":
          fav_list.books.add(book)
        elif action == "remove":
          fav_list.books.remove(book)
        return redirect(reverse("books:book",kwargs={"pk":pk}))
      except Book.DoesNotExist:
        return redirect(reverse("core:home"))
  else:
    return redirect(reverse("core:home"))

  
class SeeFavsView(TemplateView):
  template_name = "favs/fav_list.html"