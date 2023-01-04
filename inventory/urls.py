from .views import inventory_list,per_product_view,add_product_view
from django.urls import path


# namespace = "inventory"

urlpatterns = [
    path("", inventory_list, name="index"),
    path("product/<int:pk>", per_product_view, name="product"),
    path("add/", add_product_view, name="add"),
]
