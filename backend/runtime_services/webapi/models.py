from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class Blob(models.Model):
    class Meta:
        verbose_name_plural = 'Blobs'
    
    id = models.BigIntegerField(primary_key=True)
    content = models.BinaryField(editable=True)
    name = models.CharField(max_length=120)
    uploadedAt = models.DateTimeField(auto_now_add=True)
    

class UserProfile(AbstractUser):
    class Meta:
        verbose_name_plural = 'UserProfiles'

    enablePdfToImage = models.BooleanField(default=False)
    enableJobApplicationTracker = models.BooleanField(default=False)

    profileImage = models.ForeignKey(Blob, on_delete=models.PROTECT, related_name='profile_pic', null=True, default=None, blank=True)


class Company(models.Model):
    class Meta:
        verbose_name_plural = 'Companies'

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField()
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50, null=True, default=None, blank=True)
    country = models.CharField(max_length=50, null=True, default=None, blank=True)
    zipCode = models.CharField(max_length=50, null=True, default=None, blank=True)
    email = models.CharField(max_length=100)
    portal = models.CharField(max_length=500)
    profile = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name='profile', default=None)

    def __str__(self):
        return(f"Company: {self.name} | Email: {self.email} | Portal: {self.portal}")
    

class ApplicationStatus(models.Model):
    class Meta:
        verbose_name_plural = 'ApplicationStatuses'

    name = models.CharField(max_length=50)

    def __str__(self):
        return(f"Status: {self.name}")
    

class JobApplication(models.Model):
    class Meta:
        verbose_name_plural = 'JobApplications'

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField()
    role = models.CharField(max_length=50)
    ctc = models.IntegerField(blank=True)
    currency = models.CharField(max_length=10, null=True, default=None, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='company', default=None)
    status = models.ForeignKey(ApplicationStatus, on_delete=models.PROTECT, related_name='status')
    officeLocation = models.CharField(max_length=50, null=True, default=None, blank=True)

    def __str__(self):
        return(f"Company: {self.company.name} | Role: {self.role} | Status: {self.status.name}")