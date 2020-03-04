
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job (models.Model):

    jobtype = (
        ("CDD", "CDD"),
        ("CDI", "CDI"),
        ("Interim","Interim"),
        ("Freelance","Freelance")
    )

    Categories = (
        ("enseignement","Enseignement education"),
        ("earketing","Marketing"),
        ("eelemarketing","Telemarketing"),
        ("software","Developpement d'application & web"),
        ("batiment","Batiments et design"),
        ("administration","Administration"),
        ("autre","Autres")
    )

    Experiences = (
        ("non","Non spécifié"),
        ("Debutant","Debutant"),
        ("junior","1 à 2 ans d'experiences"),
        ("moyen", "2 à 6 ans d'experiences"),
        ("senior","plus de 6 ans d'experiences")
    )

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
    img_profil = models.FileField(upload_to="img/candiateds", default = "img/svg_icon/1.svg")
    register_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username

class Candidat(models.Model):
    compte = models.OneToOneField(Compte, on_delete=models.CASCADE)
    qualifications = models.CharField(max_length=100)

    def __str__(self):
        return self.compte
    
    def is_connected(self):
        return compte.user.last_login
    
    
    
