from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Compte)
class CompteAdmin(admin.ModelAdmin):
    pass

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["titre","posteur","pub_date","type"]


@admin.register(Candidat)
class CandidatAdmin(admin.ModelAdmin):
    pass

@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    pass