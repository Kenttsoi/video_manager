from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=200)
    code_primany = models.CharField(max_length=20, unique=True)
    code_alt = models.CharField(max_length=20, unique=True, null=True, blank=True)
    actors = models.ManyToManyField('Actor', related_name='videos')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    release_month = models.DateField(null=True, blank=True)
    path = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title