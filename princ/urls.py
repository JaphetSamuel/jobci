from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("jobs/", views.JobListView.as_view(), name="joblist"),
    path("details/<int:pk>/", views.JobDetailsView.as_view(), name="job-details")
]
