from django.db import models

# Create your models here.


class Project(models.Model):
    sponsor = models.TextField()
    title = models.TextField()
    link = models.CharField(max_length=300)
    amount = models.CharField(max_length=100, null=True)
    deadline = models.DateField(blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    active = models.CharField(max_length=1, default='Y')


