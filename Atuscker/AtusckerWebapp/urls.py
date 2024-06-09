from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product_list", views.product_list, name="product_list"),
    path("specific_product", views.specific_product, name="specific_product")
]