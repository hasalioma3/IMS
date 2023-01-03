from .views import index
from django.urls import path


# namespace = "inventory"

urlpatterns = [
    path("", index, name="index"),
]
