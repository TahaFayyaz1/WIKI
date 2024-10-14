from django.urls import path
from . import util
from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("createnewpage", views.create_new_page, name="create_new_page"),
    path("random", views.random_entry, name="random_entry"),
    path("editpage<str:title>", views.edit_page, name="edit_page"),
    path("wiki/<str:title>", views.display_content, name="display_content")
]

