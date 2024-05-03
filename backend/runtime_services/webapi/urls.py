from django.urls import path
from .views import main, pdf_to_image, companies, company, jobApplicationsByCompanyAndApplication, jobApplicationsByCompany, jobApplications

urlpatterns = [
    path("", main),
    path("pdf-to-image/", pdf_to_image),
    path("companies/<int:companyId>/", company),
    path("companies/", companies),
    path("companies/<int:companyId>/jobs-applications/<int:jobApplicationId>/", jobApplicationsByCompanyAndApplication),
    path("companies/<int:companyId>/jobs-applications/", jobApplicationsByCompany),
    path("jobs-applications/", jobApplications)
]
