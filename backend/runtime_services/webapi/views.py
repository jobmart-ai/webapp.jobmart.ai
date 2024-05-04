from django.http import HttpResponse, JsonResponse
from controllers import pdf_to_image_controller, companies_controller, job_applications_controller
from django.views.decorators.csrf import csrf_exempt
import json

utilities = [
    {
        "name": "Convert PDF to Image",
        "path": "/api/pdf-to-image",
        "Description" : "Convert a DPF to a JPEG or PNG wrapped inside a ZIP"
    },
    {
        "name": "List all Companies",
        "path": "/api/companies",
        "Description" : "View all companies"
    },
    {
        "name": "List all Job Applications",
        "path": "/api/jobs-applications",
        "Description" : "View all applications"
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
def companies(request):
    return genericRequestHandler(request, {
        "GET": companies_controller.getAll,
        "POST": companies_controller.post
    })

@csrf_exempt
def company(request, companyId):
    return genericRequestHandler(request, {
        "GET": companies_controller.get,
        "PATCH": companies_controller.patch,
        "DELETE": companies_controller.delete
    }, companyId)

@csrf_exempt
def jobApplicationsByCompany(request, companyId):
    return genericRequestHandler(request, {
        "GET": job_applications_controller.getByCompanyId
    }, companyId)

@csrf_exempt
def jobApplicationsByCompanyAndApplication(request, companyId, jobApplicationId):
    return genericRequestHandler(request, {
        "GET": job_applications_controller.getByCompanyIdAndApplicationId 
    }, companyId, jobApplicationId)

@csrf_exempt
def jobApplications(request):
    return genericRequestHandler(request, {
        "GET": job_applications_controller.getAll 
    })

def genericRequestHandler(request, methodMap, *args):
    handler = methodMap.get(request.method)
    if handler:
        return handler(request, *args)
    
    return HttpResponse(request.method + ' not supported', status=404)