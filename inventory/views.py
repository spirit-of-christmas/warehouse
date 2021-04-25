from django.conf import settings
from django.http import HttpResponse
import dropbox

from .barcodes import BarCode


def index(request):
    return HttpResponse("Hello World")

def barcode(request):
    code = request.GET.get("code", "0" * 13)
    barcode = BarCode(code)
    binaryStuff = barcode.asString("gif")
    dbx = dropbox.Dropbox(settings.DROPBOX_OAUTH2_TOKEN)
    dbx.files_upload(binaryStuff, f"/{code}.gif")
    print(dbx.files_get_metadata(f"/{code}.gif").server_modified)

    return HttpResponse(binaryStuff, "image/gif")
