from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *
from django.contrib.auth.views import LoginView


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
        context["nb_query"] = self.queryset.count()
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
            
            if experience != "-":
                qs2 = Job.objects.filter(experience__icontains=experience)
                self.queryset.intersection(qs2)
            
            if categorie != "-":
                qs3 = Job.objects.filter(categorie__icontains=categorie)
                self.queryset.intersection(qs3)
            
        return super().get(request,**kwargs)


class JobDetailsView(DetailView):
    model = Job
    template_name = 'princ/job_detail.html'
    context_object_name = 'job'

class CandidatDetailsView(DetailView):
    template_name = "registration/profile.html"
    context_object_name = "can"
    model = Candidat

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user and self.request.user == self.get_object().user:
            context["own"] = True
        return context

def Applymiddleware(request, id_job):
    _job = Job.objects.get(id=id_job)
    _candidat = request.user.candidat
    apply = Apply.objects.create(candidat=_candidat, job = _job)
    apply.save()
    return redirect(f"/candidat/details/{_candidat.id}")