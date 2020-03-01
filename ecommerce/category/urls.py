from django.urls import path
from .views import *

urlpatterns = [
    path("",all,name='cat-home'),
    path("create/",create,name="cat-create"),
    path("edit/",edit,name="cat-edit"),
    path("delete/",delete,name="cat-delete")
]