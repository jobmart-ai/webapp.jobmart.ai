from rest_framework import serializers
from webapi.models import UserProfile, Blob
from serializers.blob_serializer import BlobSerializer

class UserProfileRegistrationSerializer(serializers.ModelSerializer):
    profileImage = BlobSerializer(required=False)

    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'email', 'enablePdfToImage', 'enableJobApplicationTracker', 'profileImage']

    def create(self, validated_data):
        profile_image_data = validated_data.pop('profileImage', None)
        user_profile = UserProfile.objects.create(**validated_data)

        if profile_image_data:
            profile_image = Blob.objects.create(**profile_image_data)
            user_profile.profileImage = profile_image
            user_profile.save()

        return user_profile

    def update(self, entity, validated_data):
        profile_image_data = validated_data.pop('profileImage', None)
        for attr, value in validated_data.items():
            setattr(entity, attr, value)

        if profile_image_data:
            profile_image = Blob.objects.create(**profile_image_data)
            entity.profileImage = profile_image

        entity.save()
        return entity