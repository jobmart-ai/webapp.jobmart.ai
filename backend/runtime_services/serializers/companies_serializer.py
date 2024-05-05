from rest_framework import serializers
from webapi.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'state', 'country', 'zipCode', 'email', 'portal']