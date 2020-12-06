from django.urls import path
from .views import create_reviews

app_name="reviews"

urlpatterns=[
  path("create/<int:pk>",create_reviews,name="create"),
]