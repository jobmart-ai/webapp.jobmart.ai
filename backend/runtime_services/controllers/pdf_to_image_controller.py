from django.http import HttpResponse, JsonResponse
from services.pfd_to_image.main import PDFToImageConverter

get_reponse = {
    "method": "POST",
    "url" : "/api/pdf-to-image",
    "params": {
        "name": "",
        "format": ""
    },
    "body": ""
}

def get(request):
    return JsonResponse(get_reponse)

def post(request):

    pdf_content = request.body
    pdf_name = request.GET.get('name')
    image_format = request.GET.get('format')

    print(pdf_name, image_format)

    if pdf_name == None or image_format == None or pdf_content == None:
        return JsonResponse(get_reponse, status=400)
    
    converter = PDFToImageConverter(pdf_name, pdf_content)
    zip_content = converter.export_as_zip(image_format)

    response = HttpResponse(zip_content, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="' + pdf_name + '.zip"'

    return response