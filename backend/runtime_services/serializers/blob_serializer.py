from rest_framework import serializers
from webapi.models import Blob

class BlobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blob
        fields = ['content', 'name']

    def create(self, validated_data):
        return Blob.objects.create(**validated_data)