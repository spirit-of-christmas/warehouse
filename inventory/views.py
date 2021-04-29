from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from . import models


class ProductSearchView(LoginRequiredMixin, TemplateView):
    template_search_name = "inventory/product_search.html"
    template_results_name = "inventory/product_results.html"

    def get(self, request):
        return render(request, self.template_search_name, {})

    def post(self, request):
        results = []
        title = request.POST.get("title")
        keywords = request.POST.get("keywords")

        if request.POST.get("barcode"):
            results = models.Product.objects.filter(barcode_id=request.POST.get("barcode"))

        if title:
            results = results.filter(title=title) if results else models.Product.objects.filter(title=title)

        if keywords:
            tmp = [s.strip() for s in keywords.split(",")]
            results = results.filter(tags__name__in=tmp) if results else models.Product.objects.filter(tags__name__in=tmp)

        return render(request, self.template_results_name, {"results": results})


class ProductView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/product.html"

    def get(self, request, product_id):
        product = get_object_or_404(models.Product, pk=product_id)
        return render(request, self.template_name, {"product": product})
