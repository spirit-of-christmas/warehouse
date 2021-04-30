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
        search_type = request.POST.get("search-type")
        results = []

        if search_type == "barcode":
            results = models.Product.objects.filter(barcode_id=request.POST.get("query"))

        elif search_type == "title":
            results = models.Product.objects.filter(title=request.POST.get("query"))

        elif search_type == "keywords":
            results = models.Product.objects.filter(tags__name__in=[s.strip() for s in request.POST.get("query").split(",")])

        return render(request, self.template_results_name, {"results": results})


class ProductView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/product.html"

    def get(self, request, product_id):
        product = get_object_or_404(models.Product, pk=product_id)
        return render(request, self.template_name, {"product": product})
