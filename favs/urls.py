from django.urls import path
from .views import toggle_favs ,SeeFavsView

app_name="favs"

urlpatterns=[
  path("add/<int:pk>",toggle_favs,name="toggle-favs" ),
    path("my_fav_list/", SeeFavsView.as_view(), name="favs-list"),

]