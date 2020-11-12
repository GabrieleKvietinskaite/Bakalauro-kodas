from rest_framework import serializers

from .models import Competence, Player, Role, Scenario, Question, Answer, Game
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
        fields = ('id', 'scenario_id', 'question', 'is_winning', 'times_showed', 'times_lost', 'p_question')
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
        fields = ('id', 'scenario_id', 'question_id', 'number', 'answer', 'next_question_id', 'weight', 'times_chosen', 'p_answer', 'p_question_answer', 
        'availability', 'defence', 'reports', 'business', 'other')
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
            },
            'times_chosen': {
                # Tell DRF that the link field is not required.
                'required': False,
            },
            'p_answer': {
                # Tell DRF that the link field is not required.
                'required': False,
            },
            'p_question_answer': {
                # Tell DRF that the link field is not required.
                'required': False,
            }
        }

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'player_id', 'scenario_id', 'questions', 'received_points', 'maximum_points', 'hypothesis', 'started_at', 'finished_at')
        extra_kwargs = {
            'questions': {
                # Tell DRF that the link field is not required.
                'required': False,
                'allow_blank': True,
            },
            'received_points': {
                # Tell DRF that the link field is not required.
                'required': False,
                'allow_blank': True,
            },
            'maximum_points': {
                # Tell DRF that the link field is not required.
                'required': False,
                'allow_blank': True,
            },
            'hypothesis': {
                # Tell DRF that the link field is not required.
                'required': False,
                'allow_blank': True,
            },
            'started_at': {
                # Tell DRF that the link field is not required.
                'required': False,
                'allow_null': True,
            },
            'finished_at': {
                # Tell DRF that the link field is not required.
                'required': False,
                'allow_null': True,
            }
        }