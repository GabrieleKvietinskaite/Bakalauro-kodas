from rest_framework import serializers

from .models import Competence, Player, Role
from rest_auth.serializers import UserDetailsSerializer

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = ('id', 'competence', 'description')

class PlayerSerializer(UserDetailsSerializer):
    competences = serializers.CharField(source = "player.competences")
    roles = serializers.CharField(source = "player.roles")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('competences', 'roles',)

    def update(self, instance, validated_data):
        player_data = validated_data.pop('player', {})
        competences = player_data.get('competences')
        roles = player_data.get('roles')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update pplayer profile
        profile = instance.player
        if player_data and competences and roles:
            profile.competences = competences
            profile.roles = roles
            profile.save()
        return instance

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'role', 'description')