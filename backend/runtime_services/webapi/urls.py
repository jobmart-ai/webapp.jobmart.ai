from django.urls import path
from .views import main, pdf_to_image, companies, company, jobApplicationsByCompanyAndApplication, jobApplicationsByCompany, jobApplications, appliationStatuses

urlpatterns = [
    path("", main),
    path("pdf-to-image/", pdf_to_image),
    path("companies/<int:companyId>/", company),
    path("companies/", companies),
    path("companies/<int:companyId>/job-applications/<int:jobApplicationId>/", jobApplicationsByCompanyAndApplication),
    path("companies/<int:companyId>/job-applications/", jobApplicationsByCompany),
    path("job-applications/", jobApplications),
    path("application-status/", appliationStatuses)
]
