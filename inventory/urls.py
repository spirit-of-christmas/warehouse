from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductSearchView.as_view(), name="search"),
    path("product/<int:product_id>/", views.ProductView.as_view(), name="product"),
]
