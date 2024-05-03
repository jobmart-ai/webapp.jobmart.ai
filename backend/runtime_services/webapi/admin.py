from django.contrib import admin
from .models import Company, ApplicationStatus, JobApplication, Blob, UserProfile

admin.site.register(UserProfile)
admin.site.register(Blob)
admin.site.register(Company)
admin.site.register(ApplicationStatus)
admin.site.register(JobApplication)

# Register your models here.
