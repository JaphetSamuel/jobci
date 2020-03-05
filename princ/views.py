from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *


# Create your views here.

def home(request):
    jobs = Job.objects.order_by("-pub_date")[:5]
    cat_list = Job.Categories
    return render(request,"home.html",context={"jobs":jobs,"cat_list":cat_list})

class JobListView(ListView):
    model = Job
    template_name = "princ/joblist.html"
    context_object_name = "jobs"
    paginate_by = 10
    allow_empty = True
    queryset = Job.objects.all().order_by("pub_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nb_jobs"] = Job.objects.count()
        context["cat_list"] = Job.Categories
        context["exp_list"] = Job.Experiences
        context["type_list"] = Job.jobtype
        return context
    
    def get(self,request,*args, **kwargs):
        #traitement de la requete
        if request.GET.__len__() >= 3:
            mot_cle = request.GET["motcle"]
            lieu = request.GET["lieu"]
            experience = request.GET["experience"]
            categorie = request.GET["categorie"]
            contrat = request.GET["contrat"]

            if contrat != "-" :
                qs1 = Job.objects.filter(type__icontains=contrat)
            
            self.queryset.intersection(qs1)
        
        
        return super().get(request,**kwargs)


class JobDetailsView(DetailView):
    model = Job
    template_name = 'princ/job_detail.html'
    context_object_name = 'job'