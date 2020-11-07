from rest_framework import generics, status
from rest_framework.response import Response
from .models import Competence, Player, Role, Scenario, Question, Answer, Game
from .serializers import CompetenceSerializer, PlayerSerializer, RoleSerializer, ScenarioSerializer, QuestionSerializer, AnswerSerializer, GameSerializer
from app.graphs import *

class CompetenceListAPIView(generics.ListCreateAPIView):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer

class PlayerListAPIView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class RoleListAPIView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class ScenarioListAPIView(generics.ListCreateAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

class QuestionListAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_object(self):
        scenario = self.kwargs.get('scenario')
        question = self.kwargs.get('question')
        
        return Question.objects.get(scenario_id=scenario, id=question)

class AnswerListAPIView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        scenario = self.kwargs.get('scenario')
        question = self.kwargs.get('question')
        
        return Answer.objects.filter(scenario_id=scenario, question_id=question) 

class AnswerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer  

    def get_object(self):
        scenario = self.kwargs.get('scenario')
        question = self.kwargs.get('question')
        answer = self.kwargs.get('answer')
        
        return Answer.objects.get(scenario_id=scenario, question_id=question, number=answer)

class GameListAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class CreateGameAPIView(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def create(self, request, *args, **kwargs):
        player = kwargs.get('player')
        scenario = kwargs.get('scenario')
        data = Game.objects.create(player_id=player, scenario_id=scenario)

        return Response(data.id, status=status.HTTP_200_OK)

class GameAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GraphAPIView(generics.GenericAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get(self, request, *args, **kwargs):
        game_id = kwargs.get('pk')
        data = Game.objects.get(id=game_id)
        graph = generate_normal_distribution(data.hypothesis)

        return Response(graph, status=status.HTTP_200_OK)

