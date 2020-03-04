# Generated by Django 3.0.3 on 2020-03-04 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('princ', '0005_compte_img_profil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualifications', models.CharField(max_length=100)),
                ('compte', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='princ.Compte')),
            ],
        ),
    ]