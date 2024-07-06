from django.db import models

# Create your models here.
class Logo(models.Model):
    langue = models.CharField(max_length=4)
    phone = models.IntegerField()
    telegram = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

class Main(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

class Detail(models.Model):
    Aviacompany = models.CharField(max_length=100)
    Duration = models.CharField(max_length=10)
    Eating = models.CharField(max_length=20)
    Viza = models.CharField(max_length=50)
    Medical_assistance = models.IntegerField()
    Experienced_highlyeducated = models.CharField(max_length=100)
    Additions = models.CharField(max_length=500)

class Country_detail(models.Model):
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    text = models.TextField()
