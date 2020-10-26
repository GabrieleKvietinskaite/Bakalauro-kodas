from rest_framework import serializers

from .models import Competence, Player, Role, Scenario, Question, Answer
from rest_auth.serializers import UserDetailsSerializer

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = ('id', 'competence', 'description')

class PlayerSerializer(UserDetailsSerializer):
    class Meta:
        model = Player
        fields = ('id', 'competences', 'roles',)
        extra_kwargs = {
            'competences': {
                # Tell DRF that the link field is not required.
                'required': False,
                'allow_blank': True,
            },
            'roles': {
                # Tell DRF that the link field is not required.
                'required': False,
                'allow_blank': True,
            }
        }

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'role', 'description')

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ('id', 'title', 'description')

class QuestionSerializer(serializers.ModelSerializer):
    scenario_id = serializers.ReadOnlyField()

    class Meta:
        model = Question
        fields = ('id', 'scenario_id', 'question', 'win', 'quantity', 'average')
        extra_kwargs = {
            'question': {
                # Tell DRF that the link field is not required.
                'required': False,
                'allow_blank': True,
            }
        }

class AnswerSerializer(serializers.ModelSerializer):
    scenario_id = serializers.ReadOnlyField()
    question_id = serializers.ReadOnlyField()
    next_question_id = serializers.ReadOnlyField()

    class Meta:
        model = Answer
        fields = ('id', 'scenario_id', 'question_id', 'number', 'answer', 'next_question_id', 'weight', 'quantity')
        extra_kwargs = {
            'number': {
                # Tell DRF that the link field is not required.
                'required': False,
            },
            'answer': {
                # Tell DRF that the link field is not required.
                'required': False,
                'allow_blank': True,
            },
            'weight': {
                # Tell DRF that the link field is not required.
                'required': False,
            }
        }