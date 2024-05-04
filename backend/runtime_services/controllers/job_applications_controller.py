import json
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from webapi.models import JobApplication, Company, ApplicationStatus
from django.core import serializers
from controllers.serializers.job_applications_serializer import JobApplicationSerializer
from rest_framework import status
from json.decoder import JSONDecodeError
from django.db.utils import IntegrityError
import datetime

def getByCompanyId(request, companyId):
    objects = JobApplication.objects.filter(company=companyId)
    if len(objects) == 0:
        return HttpResponseNotFound("JobApplication Not Found")
    
    data = serializers.serialize('json', objects)
    return HttpResponse(data, 'application/json')


def getByCompanyIdAndApplicationId(request, companyId, applicationId):
    objects = JobApplication.objects.filter(id=applicationId, company=companyId)
    if len(objects) == 0:
        return HttpResponseNotFound("JobApplication Not Found")
    
    data = serializers.serialize('json', objects)
    return HttpResponse(data, 'application/json')


def getAll(request):
    objects = JobApplication.objects.all()
    data = serializers.serialize('json', objects)
    return HttpResponse(data, 'application/json')


def postByCompanyId(request, companyId):
    company = Company.objects.filter(pk=companyId)
    if len(company) == 0:
        return HttpResponseNotFound("Company Not Found")
    
    try:
        model = json.loads(request.body.decode('utf-8'))
        status = ApplicationStatus.objects.filter(pk=model['status'])
        if len(status) == 0:
            return HttpResponseNotFound("ApplicationStatus Not Found")
        
        entity = JobApplicationSerializer(data=model)
        print(entity)
        if entity.is_valid():
            entity.validated_data['createdAt'] = datetime.datetime.now()
            entity.validated_data['updatedAt'] = datetime.datetime.now()
            entity.validated_data['company'] = company[0]
            entity.save()
            data = serializers.serialize('json', [entity.instance])
            return HttpResponse(data, 'application/json')
        else:
            return BadRequestHandler("Request payload failed schema validation")
    except JSONDecodeError as e:
        return BadRequestHandler(e.args[0])
    except IntegrityError as e:
        return BadRequestHandler(e.args[1])
    

def patchByCompanyIdAndApplicationId(request, companyId, jobApplicationId):
    company = Company.objects.filter(pk=companyId)
    if len(company) == 0:
        return HttpResponseNotFound("Company Not Found")
    
    objects = JobApplication.objects.filter(pk=jobApplicationId)
    if len(objects) == 0:
        return HttpResponseNotFound("JobApplication Not Found")
    
    try:
        model = json.loads(request.body.decode('utf-8'))
        status = ApplicationStatus.objects.filter(pk=model['status'])
        if len(status) == 0:
            return HttpResponseNotFound("ApplicationStatus Not Found")
        
        entity = JobApplicationSerializer(data=model)
        savedEntity = objects[0]
        print(entity)
        if entity.is_valid():
            savedEntity.updatedAt = datetime.datetime.now()
            savedEntity.role = entity.validated_data['role']
            savedEntity.ctc = entity.validated_data['ctc']
            savedEntity.currency = entity.validated_data['currency']
            savedEntity.officeLocation = entity.validated_data['officeLocation']
            savedEntity.status = entity.validated_data['status']
            savedEntity.save()
            data = serializers.serialize('json', [savedEntity])
            return HttpResponse(data, 'application/json')
        else:
            return BadRequestHandler("Request payload failed schema validation")
    except JSONDecodeError as e:
        return BadRequestHandler(e.args[0])
    except IntegrityError as e:
        return BadRequestHandler(e.args[1])
    

def deleteByCompanyIdAndApplicationId(request, companyId, jobApplicationId):
    company = Company.objects.filter(pk=companyId)
    if len(company) == 0:
        return HttpResponseNotFound("Company Not Found")
    
    objects = JobApplication.objects.filter(pk=jobApplicationId)
    if len(objects) == 0:
        return HttpResponseNotFound("JobApplication Not Found")
    
    entity = objects[0]
    entity.delete()
    data = serializers.serialize('json', objects)
    return HttpResponse(data, 'application/json')
    

def BadRequestHandler(e):
    error = {
        "message": e,
        "schema": {
            "role" : "",
            "ctc": 0,
            "currency": "",
            "officeLocation": "",
            "status": 0
        }
    }
    return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)