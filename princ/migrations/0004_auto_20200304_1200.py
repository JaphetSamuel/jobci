# Generated by Django 3.0.3 on 2020-03-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('princ', '0003_auto_20200304_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='categorie',
            field=models.CharField(blank=True, choices=[('enseignement', 'Enseignement education'), ('earketing', 'Marketing'), ('eelemarketing', 'Telemarketing'), ('software', "Developpement d'application & web"), ('batiment', 'Batiments et design'), ('administration', 'Administration'), ('autre', 'Autres')], default='autre', max_length=200),
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.CharField(blank=True, choices=[('non', 'Non spécifié'), ('Debutant', 'Debutant'), ('junior', "1 à 2 ans d'experiences"), ('moyen', "2 à 6 ans d'experiences"), ('senior', "plus de 6 ans d'experiences")], default='None', max_length=100),
        ),
    ]