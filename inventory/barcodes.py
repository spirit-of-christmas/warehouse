from reportlab.lib.units import mm
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import HorizontalBarChart


class BarCode(Drawing):
    def __init__(self, text_value, *args, **kw):
        barcode = createBarcodeDrawing(
            "EAN13",
            value=text_value,
            barHeight=14 * mm,
            humanReadable=True,
            barWidth=1 * mm,
        )

        Drawing.__init__(self, barcode.width, barcode.height, *args, **kw)
        self.add(barcode, name="barcode")
