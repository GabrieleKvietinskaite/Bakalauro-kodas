from rest_framework import generics
from .models import Competence, Player, Role
from .serializers import CompetenceSerializer, PlayerSerializer, RoleSerializer

class CompetenceAPIView(generics.ListCreateAPIView):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer

class PlayerListAPIView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class RoleAPIView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer