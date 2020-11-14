from django.db import models
from django.contrib.auth.models import AbstractUser

class Competence(models.Model):
    competence = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.competence

class Role_level(models.Model):
    level = models.CharField(max_length = 100)
    points_from = models.DecimalField(max_digits=7, decimal_places=5)
    points_to = models.DecimalField(max_digits=7, decimal_places=5)

class Player(AbstractUser):
    competences = models.CharField(max_length = 100)
    roles = models.CharField(max_length = 100)
    level = models.ForeignKey(Role_level, related_name='player', on_delete=models.CASCADE)

class Role(models.Model):
    role = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.role

class Scenario(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    level = models.ForeignKey(Role_level, related_name='scenarios', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Question(models.Model):
    scenario = models.ForeignKey(Scenario, related_name='questions', on_delete=models.CASCADE)
    question = models.CharField(max_length = 500)
    is_winning = models.BooleanField(null=True)
    times_showed = models.IntegerField()
    times_lost = models.IntegerField()
    p_question = models.DecimalField(max_digits=3, decimal_places=2)
    availability = models.IntegerField()
    defence = models.IntegerField()
    reports = models.IntegerField()
    business = models.IntegerField()
    other = models.IntegerField()

    def __str__(self):
        return self.question

class Answer(models.Model):
    scenario = models.ForeignKey(Scenario, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    number = models.IntegerField()
    answer = models.CharField(max_length = 500)
    next_question = models.ForeignKey(Question, related_name='next_answers', on_delete=models.CASCADE)
    times_chosen = models.IntegerField()
    p_answer = models.DecimalField(max_digits=3, decimal_places=2)
    p_question_answer = models.DecimalField(max_digits=3, decimal_places=2)

    
class Game(models.Model):
    player = models.ForeignKey(Player, related_name='games', on_delete=models.CASCADE)
    scenario = models.ForeignKey(Scenario, related_name='games', on_delete=models.CASCADE)
    questions = models.CharField(max_length = 100)
    maximum_points = models.CharField(max_length = 100)
    received_points = models.CharField(max_length = 100)
    level_before = models.ForeignKey(Role_level, related_name='games', on_delete=models.CASCADE, null=True)
    level_after = models.ForeignKey(Role_level, related_name='after_games', on_delete=models.CASCADE, null=True)
    results = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)
    