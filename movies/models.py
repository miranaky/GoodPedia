from django.urls import reverse
from django.db import models
from core.models import CoreModel


class Movie(CoreModel):

    """ Movie Model """

    title = models.CharField(max_length=120)
    year = models.IntegerField()
    cover_image = models.ImageField(
        null=True, blank=True, upload_to='images/movies/')
    rating = models.IntegerField(default=0)
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="movies")
    director = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="movies")
    cast = models.ManyToManyField("people.Person", related_name="c_movies")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movies:movie", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating
            return round(all_ratings / len(all_reviews), 2)
        return 0

    def total_reviews(self):
        return self.reviews.count()

    class Meta:
        ordering = ["-year"]
