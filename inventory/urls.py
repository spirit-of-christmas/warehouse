from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:product_id>/", views.ProductView.as_view(), name="product"),
    path("barcode/", views.barcode, name="barcode"),
]
