import base64

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from . import models
from .barcodes import BarCode


def index(request):
    return HttpResponse("Hello World")

class ProductView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/product.html"

    def get(self, request, product_id):
        product = get_object_or_404(models.Product, pk=product_id)
        return render(request, self.template_name, {"product": product})

def barcode(request):
    code = request.GET.get("code", "0" * 13)
    bc = BarCode(code).save()
    return HttpResponse(bc, "image/gif")
