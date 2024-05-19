from rest_framework import serializers
from webapi.models import UserProfile

class UserProfileRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'email', 'enablePdfToImage', 'enableJobApplicationTracker']