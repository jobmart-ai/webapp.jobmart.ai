from django.http import HttpResponse
from webapi.models import ApplicationStatus
from django.core import serializers

def getAll(request):
    objects = ApplicationStatus.objects.all()
    data = serializers.serialize('json', objects)
    return HttpResponse(data, 'application/json')