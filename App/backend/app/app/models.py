from django.db import models
from django.contrib.auth.models import User

class Competence(models.Model):
    competence = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.competence

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    competences = models.CharField(max_length = 100)
    roles = models.CharField(max_length = 100)

    def __str__(self):
        return self.user

class Role(models.Model):
    role = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.role