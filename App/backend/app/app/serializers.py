from rest_framework import serializers

from .models import Competence, Role_level, Player, Role, Scenario, Question, Answer, Game
from rest_auth.serializers import UserDetailsSerializer

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = ('id', 'competence', 'description')

class Role_levelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role_level
        fields = ('id', 'level', 'points_from', 'points_to')

class RoleSerializer(serializers.ModelSerializer):
    competences = CompetenceSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = ('id', 'role', 'description', 'competences')

class RoleWCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'role', 'description')

class PlayerSerializer(UserDetailsSerializer):
    role = RoleWCSerializer()
    level = Role_levelSerializer()

    class Meta:
        model = Player
        fields = ('id', 'competences', 'role', 'level')
        extra_kwargs = {
            'competences': {
                # Tell DRF that the link field is not required.
                'required': False,
                'allow_blank': True,
            },
            'role': {
                # Tell DRF that the link field is not required.
                'required': False,
                'allow_blank': True,
            }
        }

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ('id', 'title', 'description', 'level')

class QuestionSerializer(serializers.ModelSerializer):
    scenario_id = serializers.ReadOnlyField()

    class Meta:
        model = Question
        fields = ('id', 'scenario_id', 'question', 'is_winning', 'times_showed', 'times_lost', 'p_question',
        'availability', 'defence', 'reports', 'business', 'other')
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
        fields = ('id', 'scenario_id', 'question_id', 'number', 'answer', 'next_question_id', 'times_chosen', 'p_answer', 'p_question_answer')
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
        fields = ('id', 'player_id', 'scenario_id', 'questions', 'received_points', 'maximum_points', 
        'level_before', 'level_after', 'report', 'started_at', 'finished_at')
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
            'level_before': {
                # Tell DRF that the link field is not required.
                'required': False,
            },
            'level_after': {
                # Tell DRF that the link field is not required.
                'required': False,
            },
            'results': {
                # Tell DRF that the link field is not required.
                'required': False,
            },
            'report': {
                # Tell DRF that the link field is not required.
                'required': False,
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