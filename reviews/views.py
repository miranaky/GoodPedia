from django.shortcuts import redirect, reverse
from .forms import CreateReviewForm
from movies.models import Movie
from books.models import Book

# Create your views here.
def create_reviews(request,pk):
  the_type = request.GET.get("type")
  if request.method == "POST":
    form =CreateReviewForm(request.POST)
    if the_type == "movie":
      try:
        movie = Movie.objects.get(pk=pk)
        if form.is_valid():
          review = form.save()
          review.movie=movie
          review.created_by=request.user
          review.save()
          return redirect(reverse("movies:movie",kwargs={"pk":movie.pk}))
      except Movie.DoesNotExist:
        return redirect(reverse("core:home"))
    elif the_type == "book":
      try:
        book = Book.objects.get(pk=pk)
        if form.is_valid():
          review = form.save()
          review.book=book
          review.created_by=request.user
          review.save()
          return redirect(reverse("books:book",kwargs={"pk":book.pk}))
      except Book.DoesNotExist:
        return redirect(reverse("core:home"))
    else:
      print("error for checking type")
