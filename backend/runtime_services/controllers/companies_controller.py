import json
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from webapi.models import Company
from django.core import serializers
from serializers.companies_serializer import CompanySerializer
from json.decoder import JSONDecodeError
from django.db.utils import IntegrityError
from django.forms.models import model_to_dict
import datetime


def get(request, companyId):
    objects = Company.objects.filter(pk=companyId, profile=request.user)
    if len(objects) == 0:
        return HttpResponseNotFound("Company Not Found")
    
    data = model_to_dict(objects[0])
    return JsonResponse(data)


def getAll(request):
    objects = Company.objects.filter(profile=request.user)
    data = serializers.serialize('json', objects)
    return HttpResponse(data, 'application/json')


def post(request):
    try:
        model = json.loads(request.body.decode('utf-8'))
        entity = CompanySerializer(data=model)
        
        if entity.is_valid():
            entity.validated_data['createdAt'] = datetime.datetime.now()
            entity.validated_data['updatedAt'] = datetime.datetime.now()
            entity.validated_data['profile_id'] = request.user.id
            entity.save()
            data = model_to_dict(entity.instance)
            return JsonResponse(data)
        else:
            return BadRequestHandler("Request payload failed schema validation")
    except JSONDecodeError as e:
        return BadRequestHandler(e.args[0])
    except IntegrityError as e:
        return BadRequestHandler(e.args[1])
    

def patch(request, companyId):
    objects = Company.objects.filter(pk=companyId)
    if len(objects) == 0:
        return HttpResponseNotFound("Company Not Found")
    
    try:
        model = json.loads(request.body.decode('utf-8'))
        entity = CompanySerializer(data=model)
        savedEntity = objects[0]
        
        if entity.is_valid():
            savedEntity.updatedAt = datetime.datetime.now()
            savedEntity.name = entity.validated_data['name']
            savedEntity.state = entity.validated_data['state']
            savedEntity.country = entity.validated_data['country']
            savedEntity.zipCode = entity.validated_data['zipCode']
            savedEntity.email = entity.validated_data['email']
            savedEntity.portal = entity.validated_data['portal']
            savedEntity.save()
            data = model_to_dict(savedEntity)
            return JsonResponse(data)
        else:
            return BadRequestHandler("Request payload failed schema validation")
    except JSONDecodeError as e:
        return BadRequestHandler(e.args[0])
    except IntegrityError as e:
        return BadRequestHandler(e.args[1])
    
        
def delete(request, companyId):
    objects = Company.objects.filter(pk=companyId)
    if len(objects) == 0:
        return HttpResponseNotFound("Company Not Found")
    
    entity = objects[0]
    data = model_to_dict(entity)
    entity.delete()
    return JsonResponse(data)

    
def BadRequestHandler(e):
    error = {
        "message": e,
        "schema": {
            "name" : "",
            "state": "",
            "country": "",
            "zipCode": "",
            "email": "",
            "portal": ""
        }
    }
    return JsonResponse(error, status=400)
    