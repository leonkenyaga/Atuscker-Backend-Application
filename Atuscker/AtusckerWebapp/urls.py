from django.urls import path


from . import views
from .views import ProductUpdateView

urlpatterns = [
    path("product_list", views.product_list, name="product_list"),
    path('products/<int:pk>/', views.product_detail),
    path('productimage_list', views.productimage_list),
    path('productimages/<int:pk>', views.productimage_detail),
    path('productwithimages/<int:pk>', views.productwithimages),
    path('specificproductimages/<int:pk>', views.specificproductimages),
    path('specificCategoryproducts/<int:pk>', views.specificCategoryproducts),
    path('productupdate/<int:pk>/', ProductUpdateView)
]
