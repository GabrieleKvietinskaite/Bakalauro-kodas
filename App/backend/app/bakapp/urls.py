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
from django.views.generic.base import TemplateView

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
    url(r'api/scenarios/(?P<role>[0-9]+)/(?P<level>[0-9]+)$', views.ScenarioListAPIView.as_view(), name='scenarios-list'),

    # PLAYER
    url(r'api/player/(?P<pk>[0-9]+)$', views.PlayerAPIView.as_view()),

    url(r'api/player/(?P<player>[0-9]+)/games$', views.PlayerGamesAPIView.as_view()),

    # QUESTION
    url(r'^api/scenario/(?P<scenario>[0-9]+)/question/(?P<question>[0-9]+)$', views.QuestionAPIView.as_view()),

    # ANSWER
    url(r'^api/scenario/(?P<scenario>[0-9]+)/question/(?P<question>[0-9]+)/answers$', views.AnswerListAPIView.as_view(), name='answers-list'),
    url(r'^api/scenario/(?P<scenario>[0-9]+)/question/(?P<question>[0-9]+)/answer/(?P<answer>[0-9]+)/update$', views.AnswerQuantityAPIView.as_view()),
    
    # GAME
    path(r'api/games', views.GameListAPIView.as_view(), name='games-list'),
    url(r'api/game/(?P<pk>[0-9]+)/results$', views.ResultsAPIView.as_view()),
    url(r'api/game/player/(?P<player>[0-9]+)/scenario/(?P<scenario>[0-9]+)/create$', views.CreateGameAPIView.as_view()),
    url(r'api/game/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)$', views.GameAPIView.as_view()),
    url(r'api/game/(?P<pk>[0-9]+)$', views.GameAPIView.as_view()),

    url(r'^.*', TemplateView.as_view(template_name="home.html"), name="home")
]