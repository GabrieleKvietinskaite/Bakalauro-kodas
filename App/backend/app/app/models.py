from django.db import models
from django.contrib.auth.models import AbstractUser

class Competence(models.Model):
    competence = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.competence

class Player(AbstractUser):
    competences = models.CharField(max_length = 100)
    roles = models.CharField(max_length = 100)

    def __str__(self):
        return self.competences

class Role(models.Model):
    role = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.role

class Scenario(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.title