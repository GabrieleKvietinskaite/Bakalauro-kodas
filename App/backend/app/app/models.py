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

class Question(models.Model):
    scenario = models.ForeignKey(Scenario, related_name='questions', on_delete=models.CASCADE)
    question = models.CharField(max_length = 500)
    is_winning = models.BooleanField(null=True)
    times_showed = models.IntegerField()
    times_lost = models.IntegerField()
    p_question = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.question

class Answer(models.Model):
    scenario = models.ForeignKey(Scenario, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    number = models.IntegerField()
    answer = models.CharField(max_length = 500)
    next_question = models.ForeignKey(Question, related_name='next_answers', on_delete=models.CASCADE)
    weight = models.IntegerField()
    times_chosen = models.IntegerField()
    p_answer = models.DecimalField(max_digits=3, decimal_places=2)
    p_question_answer = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.answer

class Game(models.Model):
    player = models.ForeignKey(Player, related_name='games', on_delete=models.CASCADE)
    scenario = models.ForeignKey(Scenario, related_name='games', on_delete=models.CASCADE)
    questions = models.CharField(max_length = 100)
    received_points = models.CharField(max_length = 100)
    maximum_points = models.CharField(max_length = 100)
    hypothesis = models.CharField(max_length = 100)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.questions
    