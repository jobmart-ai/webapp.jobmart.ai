from django.http import HttpResponse
from controllers import pdf_to_image_controller, companies_controller, job_applications_controller, application_status_controller, user_profiles_controller
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
        "path": "/api/job-applications",
        "Description" : "View all applications"
    },
    {
        "name": "List all Application Stauts",
        "path": "/api/application-status",
        "Description" : "View all stauts"
    },
    {
        "name": "Get authenticated Users",
        "path": "/api/user",
        "Description" : "View active users"
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
    }, False)

@csrf_exempt
def companies(request):
    return genericRequestHandler(request, {
        "GET": companies_controller.getAll,
        "POST": companies_controller.post
    }, False)

@csrf_exempt
def company(request, companyId):
    return genericRequestHandler(request, {
        "GET": companies_controller.get,
        "PATCH": companies_controller.patch,
        "DELETE": companies_controller.delete
    }, False, companyId)

@csrf_exempt
def jobApplicationsByCompany(request, companyId):
    return genericRequestHandler(request, {
        "GET": job_applications_controller.getByCompanyId,
        "POST": job_applications_controller.postByCompanyId
    }, False, companyId)

@csrf_exempt
def jobApplicationsByCompanyAndApplication(request, companyId, jobApplicationId):
    return genericRequestHandler(request, {
        "GET": job_applications_controller.getByCompanyIdAndApplicationId,
        "PATCH": job_applications_controller.patchByCompanyIdAndApplicationId,
        "DELETE": job_applications_controller.deleteByCompanyIdAndApplicationId
    }, False, companyId, jobApplicationId)

@csrf_exempt
def jobApplications(request):
    return genericRequestHandler(request, {
        "GET": job_applications_controller.getAll 
    }, False)

@csrf_exempt
def appliationStatuses(request):
    return genericRequestHandler(request, {
        "GET": application_status_controller.getAll 
    }, False)

@csrf_exempt
def userLogin(request):
    return genericRequestHandler(request, {
        "POST": user_profiles_controller.signin 
    }, True)

@csrf_exempt
def userLogout(request):
    return genericRequestHandler(request, {
        "POST": user_profiles_controller.signout 
    }, True)

@csrf_exempt
def user(request):
    return genericRequestHandler(request, {
        "GET": user_profiles_controller.get,
        "POST": user_profiles_controller.register,
        "DELETE": user_profiles_controller.delete
    }, True)

def genericRequestHandler(request, methodMap, sikpAuth, *args):
    handler = methodMap.get(request.method)
    if handler:
        if authValidator(request, sikpAuth):
            return handler(request, *args)
        else:
            return HttpResponse('User Unauthorized', status=401)
    
    return HttpResponse(request.method + ' not supported', status=404)


def authValidator(request, skipAuth):
    if skipAuth is True:
        return True
    
    if request.user.is_authenticated:
        print('User Authorized')
        return True
    else:
        print('User Unauthorized')
        return False
        