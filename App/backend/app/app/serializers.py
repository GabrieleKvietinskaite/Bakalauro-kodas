from rest_framework import serializers

from .models import Competence, Player, Role

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = ('id', 'competence', 'description')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('user', 'competences', 'roles')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'role', 'description')