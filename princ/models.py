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

    posteur = models.ForeignKey('Compte', on_delete= models.CASCADE, blank=True)
    titre = models.CharField(max_length=200, blank=False)
    lieu = models.CharField(max_length=200)
    type = models.CharField(max_length=100, choices=jobtype)
    pub_date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    salaire_max = models.IntegerField(null=True)
    salaire_min = models.IntegerField(null=True)

    def __str__(self):
        return self.titre
    

class Compte(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    register_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    
