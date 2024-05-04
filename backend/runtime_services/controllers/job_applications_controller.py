import json
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from webapi.models import JobApplication
from django.core import serializers

def getByCompanyId(request, companyId):
    objects = JobApplication.objects.filter(company=companyId)
    if len(objects) == 0:
        return HttpResponseNotFound("Not Found")
    
    data = serializers.serialize('json', objects)
    return HttpResponse(data, 'application/json')

def getByCompanyIdAndApplicationId(request, companyId, applicationId):
    objects = JobApplication.objects.filter(id=applicationId, company=companyId)
    if len(objects) == 0:
        return HttpResponseNotFound("Not Found")
    
    data = serializers.serialize('json', objects)
    return HttpResponse(data, 'application/json')

def getAll(request):
    objects = JobApplication.objects.all()
    if len(objects) == 0:
        return HttpResponseNotFound("Not Found")
    
    data = serializers.serialize('json', objects)
    return HttpResponse(data, 'application/json')

def post(request):
    return JsonResponse('hi')