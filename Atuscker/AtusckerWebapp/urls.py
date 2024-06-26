from django.urls import path

from . import views

urlpatterns = [
    path("product_list", views.product_list, name="product_list"),
    path('products/<int:pk>/', views.product_detail),
    path('productimage_list', views.productimage_list),
    path('productimages/<int:pk>', views.productimage_detail),
    path('productwithimage/<int:pk>', views.productwithimages),
    path('specificproductimages/<int:pk>', views.specificproductimages) 
]
