from django.http import HttpResponse, JsonResponse
from controllers import pdf_to_image_controller, job_application_tracker_controller
from django.views.decorators.csrf import csrf_exempt
import json

utilities = [
    {
        "name": "Convert PDF to Image",
        "path": "/api/pdf-to-image",
        "Description" : "Convert a DPF to a JPEG or PNG wrapped inside a ZIP"
    },
    {
        "name": "Job Application Tracker",
        "path": "/api/job-application-tracker",
        "Description" : "Add, manage and monitor Job Applications"
    }
]

# Create your views here.
def main(request):
    return HttpResponse(json.dumps(utilities), content_type='application/json')

@csrf_exempt
def pdf_to_image(request):
    return genericRequestHandler(request, {
        "GET": pdf_to_image_controller.get,
        "POST": pdf_to_image_controller.post
    })

@csrf_exempt
def job_application_tracker(request):
    return genericRequestHandler(request, {
        "GET": job_application_tracker_controller.get,
        "POST": job_application_tracker_controller.post
    })

def genericRequestHandler(request, methodMap):
    handler = methodMap.get(request.method)
    if handler:
        return handler(request)
    
    return HttpResponse(request.method + ' not supported', status=404)