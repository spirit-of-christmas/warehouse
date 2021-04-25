from django.conf import settings

from reportlab.lib.units import mm
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import HorizontalBarChart

import dropbox


class BarCode(Drawing):
    def __init__(self, value, *args, **kw):
        barcode = createBarcodeDrawing(
            "EAN13",
            value=value,
            barHeight=14 * mm,
            humanReadable=True,
            barWidth=1 * mm,
        )

        Drawing.__init__(self, barcode.width, barcode.height, *args, **kw)
        self.add(barcode, name="barcode")
        self._value = value
        self._path = f"/barcodes/{self._value}.gif"

    def save(self):
        # Do something smart here were the file is only written once, cache it or something
        binaryStuff = self.asString("gif")
        dbx = dropbox.Dropbox(settings.DROPBOX_OAUTH2_TOKEN)
        file_metadata = None

        try:
            file_metadata = dbx.files_upload(binaryStuff, self._path)

        except dropbox.exceptions.ApiError as ex:
            # Not finished fully interrogating the errors, but this seems to handle duplicates
            if all([type(ex.error) == dropbox.files.UploadError,
                    ex.error.is_path(),
                    ex.error.get_path().reason.is_conflict()]):
                print(f"File exists, probably: {ex.error.get_path().reason.get_conflict()}")

        return self._path, file_metadata
