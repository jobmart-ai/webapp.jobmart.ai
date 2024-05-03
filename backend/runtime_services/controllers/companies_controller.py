import json
from django.http import HttpResponse, JsonResponse
from webapi.models import Company
from django.core import serializers

def get(request, companyId):
    objects = Company.objects.filter(pk=companyId)
    if len(objects) == 0:
        return HttpResponseNotFound("Not Found")
    
    data = serializers.serialize('json', objects)
    return HttpResponse(data, 'application/json')

def getAll(request):
    objects = Company.objects.all()
    if len(objects) == 0:
        return HttpResponseNotFound("Not Found")
    
    data = serializers.serialize('json', objects)
    return HttpResponse(data, 'application/json')

def post(request):
    return JsonResponse('hi')