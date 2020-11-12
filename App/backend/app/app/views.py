from rest_framework import generics, status
from rest_framework.response import Response
from .models import Competence, Player, Role, Scenario, Question, Answer, Game
from .serializers import CompetenceSerializer, PlayerSerializer, RoleSerializer, ScenarioSerializer, QuestionSerializer, AnswerSerializer, GameSerializer
from app.graphs import *
from django.utils import timezone

def check(databas, request):
    if not databas:
        return request
    else:
        return databas + ';' + request

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
        query = Question.objects.filter(scenario_id=scenario, id=question)
        question_data = query.first()
        times_showed = question_data.times_showed + 1
        update = query.update(times_showed=times_showed)
        
        return Question.objects.get(scenario_id=scenario, id=question)

    def game_over(scenario, question):
        query = Question.objects.filter(scenario_id=scenario, id=question)
        data = query.first()
        question_data = query.first()
        times_lost = question_data.times_lost + 1
        update = query.update(times_lost=times_lost)
        
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

class AnswerQuantityAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer  

    def get_object(self):
        scenario = self.kwargs.get('scenario')
        question = self.kwargs.get('question')
        answer = self.kwargs.get('answer')
        query = Answer.objects.filter(scenario_id=scenario, question_id=question, number=answer)
        data = query.first()

        return query.update(times_chosen=data.times_chosen+1)

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

    def update(self, request, *args, **kwargs):
        function = kwargs.get('slug')
        game_id = kwargs.get('pk')
        query = Game.objects.filter(id=game_id)
        data = query.first()
        questions = check(data.questions, request.data['question'])

        if request.data.get('received_points') == '-1':
            QuestionAPIView.game_over(data.scenario_id, request.data['question'])

        if function == 'update':
            received_points = check(data.received_points, request.data['received_points'])
            maximum_points = check(data.maximum_points, request.data['maximum_points'])
            hypothesis = check(data.hypothesis, request.data['hypothesis'])
            update = query.update(questions=questions, received_points=received_points, maximum_points=maximum_points, hypothesis=hypothesis)

            return Response(update, status=status.HTTP_200_OK)

        elif function == 'finish':
            time = timezone.now()
            update = query.update(questions=questions, finished_at=time)

            return Response(update, status=status.HTTP_200_OK)

class GraphAPIView(generics.GenericAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get(self, request, *args, **kwargs):
            game_id = kwargs.get('pk')
            data = Game.objects.get(id=game_id)
            questions = [int(x) for x in data.questions.split(';')]
            del questions[-1]
            answers = []
            availability = []
            
            for question in questions:
                answers.append(Answer.objects.filter(scenario_id=data.scenario_id, question_id=question).values_list('times_chosen', flat=True))
                availability.append(Question.objects.filter(scenario_id=data.scenario_id, id=question).values_list('availability', flat=True))

            normal_distribution = generate_normal_distribution(data.hypothesis)
            heatmap = getHeatmap(answers)
            availability = getAvailability(availability)
            content = {'normal_distribution_graph': normal_distribution, 'answers_frequency_heatmap': heatmap, 'availability_graph': availability}

            return Response(content, status=status.HTTP_200_OK)