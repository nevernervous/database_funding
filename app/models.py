from django.db import models

# Create your models here.


class Project(models.Model):
    sponsor = models.TextField()
    title = models.TextField()
    link = models.CharField(max_length=300)
    amount = models.CharField(max_length=100, null=True)
    deadline = models.DateField(blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    active = models.CharField(max_length=1, default='Y', null=True)
    sponsor_deadline = models.DateField(blank=True, null=True)
    type = models.TextField(null=True)
    limited = models.CharField(max_length=1, default='Y')
    awards = models.TextField(null=True)


