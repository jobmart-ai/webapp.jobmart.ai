from django.urls import path
from .views import main, pdf_to_image, job_application_tracker

urlpatterns = [
    path("", main),
    path("pdf-to-image/", pdf_to_image),
    path("job-application-tracker/", job_application_tracker)
]
