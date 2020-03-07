from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("jobs/", views.JobListView.as_view(), name="joblist"),
    path("details/<int:pk>/", views.JobDetailsView.as_view(), name="job-details"),
    path("candidat/details/<int:pk>/",views.CandidatDetailsView.as_view(),name="candidate-details"),
    path("apply/<int:id_job>",views.Applymiddleware, name="apply_url"),
]
