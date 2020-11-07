"""bakapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    # AUTH
    path(r'auth/', include('rest_auth.urls')),
    path(r'auth/registration/', include('rest_auth.registration.urls')),
    path(r'auth/token/', obtain_jwt_token),
    path(r'auth/token-refresh/', refresh_jwt_token),
    path(r'auth/token-verify/', verify_jwt_token),
    # COMPETENCE
    path(r'api/competences', views.CompetenceListAPIView.as_view(), name='competences-list'),
    # ROLE
    path(r'api/roles', views.RoleListAPIView.as_view(), name='roles-list'),
    # SCENARIO
    path(r'api/scenarios', views.ScenarioListAPIView.as_view(), name='scenarios-list'),
    # PLAYER
    #path(r'api/players', views.PlayerListAPIView.as_view(), name='players-list'),
    url(r'api/player/(?P<pk>[0-9]+)$', views.PlayerAPIView.as_view()),
    # QUESTION
    #path(r'api/questions', views.QuestionListAPIView.as_view(), name='questions-list'),
    url(r'^api/scenario/(?P<scenario>[0-9]+)/question/(?P<question>[0-9]+)$', views.QuestionAPIView.as_view()),
    # ANSWER
    url(r'^api/scenario/(?P<scenario>[0-9]+)/question/(?P<question>[0-9]+)/answer/(?P<answer>[0-9]+)$', views.AnswerAPIView.as_view()),
    url(r'^api/scenario/(?P<scenario>[0-9]+)/question/(?P<question>[0-9]+)/answers$', views.AnswerListAPIView.as_view(), name='answers-list'),
    url(r'^api/scenario/(?P<scenario>[0-9]+)/question/(?P<question>[0-9]+)/answer/(?P<answer>[0-9]+)/update$', views.AnswerQuantityAPIView.as_view()),
    # GAME
    path(r'api/games', views.GameListAPIView.as_view(), name='games-list'),
    url(r'api/game/create/player/(?P<player>[0-9]+)/scenario/(?P<scenario>[0-9]+)$', views.CreateGameAPIView.as_view()),
    url(r'api/game/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)$', views.GameAPIView.as_view()),
    url(r'api/game/(?P<pk>[0-9]+)/$', views.GameAPIView.as_view()),
    url(r'api/graph/game/(?P<pk>[0-9]+)$', views.GraphAPIView.as_view()),
]