from rest_framework import serializers

from .models import Competence, Player, Role
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