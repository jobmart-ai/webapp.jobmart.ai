from django.db import models

# Create your models here.

class Company(models.Model):
    class Meta:
        verbose_name_plural = 'Companies'

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField()
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50, null=True, default=None)
    country = models.CharField(max_length=50, null=True, default=None)
    zipCode = models.CharField(max_length=50, null=True, default=None)
    email = models.CharField(max_length=100)
    portal = models.CharField(max_length=500)

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
    ctc = models.IntegerField()
    currency = models.CharField(max_length=10, null=True, default=None)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='company')
    status = models.ForeignKey(ApplicationStatus, on_delete=models.PROTECT, related_name='status')
    officeLocation = models.CharField(max_length=50, null=True, default=None)

    def __str__(self):
        return(f"Company: {self.company.name} | Role: {self.role} | Status: {self.status.name}")