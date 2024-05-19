from rest_framework import serializers
from webapi.models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['role', 'ctc', 'currency', 'status', 'officeLocation']