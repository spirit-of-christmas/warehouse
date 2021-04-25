from django.http import HttpResponse
from .barcodes import BarCode


def index(request):
    return HttpResponse("Hello World")

def barcode(request):
    d = BarCode(request.GET.get("name", "n/a"))
    binaryStuff = d.asString("gif")
    return HttpResponse(binaryStuff, "image/gif")
