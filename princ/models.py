
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job (models.Model):

    jobtype = [
        ("CDD", "CDD"),
        ("CDI", "CDI"),
        ("Interim","Interim"),
        ("Freelance","Freelance")
    ]

    Categories = [
        ("enseignement","Enseignement education"),
        ("earketing","Marketing"),
        ("eelemarketing","Telemarketing"),
        ("software","Developpement d'application & web"),
        ("batiment","Batiments et design"),
        ("administration","Administration"),
        ("autre","Autres")
    ]

    Experiences = [
        ("non","Non spécifié"),
        ("Debutant","Debutant"),
        ("junior","1 à 2 ans d'experiences"),
        ("moyen", "2 à 6 ans d'experiences"),
        ("senior","plus de 6 ans d'experiences")
    ]

    posteur = models.ForeignKey('Compte', on_delete= models.CASCADE, blank=True)
    titre = models.CharField(max_length=200, blank=False)
    categorie = models.CharField(max_length=200, blank=True, default="autre", choices=Categories)
    lieu = models.CharField(max_length=200)
    type = models.CharField(max_length=100, choices=jobtype)
    experience = models.CharField(max_length=100, choices=Experiences, blank=True, default="None")
    pub_date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    salaire_max = models.IntegerField(null=True)
    salaire_min = models.IntegerField(null=True)

    def __str__(self):
        return self.titre
    
    
    

class Compte(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    img_profil = models.FileField(upload_to="img/brand/", default = "img/svg_icon/1.svg")
    register_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username

class Candidat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    qualifications = models.CharField(max_length=100)
    img_profile = models.ImageField(upload_to="img/candiateds/", blank=True, default="img/candiateds/8.png")
    cv = models.FileField(upload_to="cv/",blank=True)
    description = models.TextField(default="vide")


    def __str__(self):
        return self.user.username

class Apply(models.Model):
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    proposition = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.candidat} a postuler pour {self.job}"
    
    
