from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    role = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

class Competence(models.Model):
    competence = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    roles = models.ManyToManyField(Role, related_name='competences', blank=True)

class Role_level(models.Model):
    level = models.CharField(max_length = 100)
    points_from = models.DecimalField(max_digits=7, decimal_places=5)
    points_to = models.DecimalField(max_digits=7, decimal_places=5)

class Player(AbstractUser):
    competences = models.CharField(max_length = 100)
    role = models.ForeignKey(Role, related_name='players', on_delete=models.CASCADE, null=True)
    level = models.ForeignKey(Role_level, related_name='players', on_delete=models.CASCADE, null=True)

class Scenario(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    level = models.ForeignKey(Role_level, related_name='scenarios', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, related_name='role_scenarios', on_delete=models.CASCADE)

class Question(models.Model):
    scenario = models.ForeignKey(Scenario, related_name='questions', on_delete=models.CASCADE)
    question = models.CharField(max_length = 500)
    is_winning = models.BooleanField(null=True)
    times_showed = models.IntegerField()
    times_lost = models.IntegerField()
    p_question = models.DecimalField(max_digits=3, decimal_places=2)
    competence = models.ForeignKey(Competence, related_name='questions', on_delete=models.CASCADE, null=True)
    availability = models.IntegerField()
    defence = models.IntegerField()
    reports = models.IntegerField()
    business = models.IntegerField()
    other = models.IntegerField()

class Answer(models.Model):
    scenario = models.ForeignKey(Scenario, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    number = models.IntegerField()
    answer = models.CharField(max_length = 500)
    next_question = models.ForeignKey(Question, related_name='next_answers', on_delete=models.CASCADE)
    times_chosen = models.IntegerField()
    p_answer = models.DecimalField(max_digits=3, decimal_places=2)
    p_question_answer = models.DecimalField(max_digits=3, decimal_places=2)
    is_competence_achieved = models.BooleanField(null=True)

class Game(models.Model):
    player = models.ForeignKey(Player, related_name='games', on_delete=models.CASCADE)
    scenario = models.ForeignKey(Scenario, related_name='games', on_delete=models.CASCADE)
    questions = models.CharField(max_length = 100)
    maximum_points = models.CharField(max_length = 100)
    received_points = models.CharField(max_length = 100)
    level_before = models.ForeignKey(Role_level, related_name='games', on_delete=models.CASCADE, null=True)
    level_after = models.ForeignKey(Role_level, related_name='after_games', on_delete=models.CASCADE, null=True)
    competences = models.CharField(max_length = 100, null=True) 
    results = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)
    report = models.FileField(null=True)
  