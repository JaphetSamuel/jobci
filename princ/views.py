from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *


# Create your views here.

def home(request):
    jobs = Job.objects.order_by("-pub_date")[:5]
    return render(request,"home.html",context={"jobs":jobs})

class JobListView(ListView):
    model = Job
    template_name = "princ/joblist.html"
    context_object_name = "jobs"
    paginate_by = 10
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nb_jobs"] = Job.objects.count()
        return context


class JobDetailsView(DetailView):
    model = Job
    template_name = 'princ/job_detail.html'
    context_object_name = 'job'