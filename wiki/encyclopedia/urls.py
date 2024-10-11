from django.urls import path
from . import util
from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.display_content, name="display_content")
]

