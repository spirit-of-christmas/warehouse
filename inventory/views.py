from django.http import HttpResponse
from reportlab.lib.units import mm
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import HorizontalBarChart

def index(request):
    return HttpResponse("Hello World")

class MyBarcodeDrawing(Drawing):
    def __init__(self, text_value, *args, **kw):
        barcode = createBarcodeDrawing('Code128', value=text_value,  barHeight=14*mm, humanReadable=True, barWidth=1*mm)
        Drawing.__init__(self,barcode.width,barcode.height,*args,**kw)       
        self.add(barcode, name='barcode')

def barcode(request):
    print(request.GET)
    d = MyBarcodeDrawing(request.GET.get("name", "n/a"))
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')
