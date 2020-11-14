from rest_framework import generics, status
from rest_framework.response import Response
from .models import Competence, Role_level, Player, Role, Scenario, Question, Answer, Game
from .serializers import CompetenceSerializer, Role_levelSerializer, PlayerSerializer, RoleSerializer, ScenarioSerializer, QuestionSerializer, AnswerSerializer, GameSerializer
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
        player_level = Player.objects.filter(id=player).values_list('level', flat=True)[0]
        data = Game.objects.create(player_id=player, scenario_id=scenario, level_before_id=player_level)

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

class ResultsAPIView(generics.GenericAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get(self, request, *args, **kwargs):
        answers = []
        availability = []
        business = []
        defence = []
        reports = []
        other = []

        game_id = kwargs.get('pk')
        query = Game.objects.filter(id=game_id)
        data = Game.objects.get(id=game_id)
        level = Role_level.objects.get(id=data.scenario.level.id)

        hypothesis = split_to_float_array(data.hypothesis, ';')
        
        
        if hypothesis[-1] != 0:
            questions = [int(x) for x in data.questions.split(';')]
            del questions[-1]
            test = []
            for question in questions:
                question_data = Question.objects.filter(scenario_id=data.scenario_id, id=question)

                answers.append(Answer.objects.filter(scenario_id=data.scenario_id, question_id=question).values_list('times_chosen', flat=True))
                availability.append(question_data.values_list('availability', flat=True)[0])
                business.append(question_data.values_list('business', flat=True)[0])
                defence.append(question_data.values_list('defence', flat=True)[0])
                reports.append(question_data.values_list('reports', flat=True)[0])
                other.append(question_data.values_list('other', flat=True)[0])

            passed = calculateLevelPass(hypothesis, level)
            if passed == 'passed':
                query.update(level_after=level.id)
                players = Player.objects.filter(level=level)
                test = Game.objects.filter(player__in=players).values_list('hypothesis', flat=True)

            test_ = []
            for x in test:
                test_.append(split_to_float_array(x, ';'))
            
            
            summed_hyp = []
            for x in test_:
                summed_hyp.append(calculateSum(x))

            query.update(results=calculateResults(availability, business, defence, reports, other))
            normal_distribution = generate_normal_distribution(summed_hyp, calculateSum(hypothesis))
            #heatmap = getHeatmap(answers)
            content = {'normal_distribution_graph': normal_distribution, 'availability_graph': getAvailability(availability), 'level': level.level, 'passed': passed}

            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response({'results': 'game over'}, status=status.HTTP_200_OK)