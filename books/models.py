from django.urls import reverse
from django.db import models
from core.models import CoreModel


class Book(CoreModel):

    """ Book Model """

    title = models.CharField(max_length=120)
    year = models.IntegerField()
    cover_image = models.ImageField(
        null=True, blank=True, upload_to='images/books/')
    rating = models.FloatField(default=0)
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="books")
    writer = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:book", kwargs={"pk": self.pk})

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
