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
    path(r'api/competences', views.CompetenceListAPIView.as_view(), name='competence-list'),
    path(r'api/player', views.PlayerListAPIView.as_view()),
    path(r'api/roles', views.RoleListAPIView.as_view(), name='role-list'),
    path(r'auth/', include('rest_auth.urls')),
    path(r'auth/registration/', include('rest_auth.registration.urls')),
    path(r'auth/token/', obtain_jwt_token),
    path(r'auth/token-refresh/', refresh_jwt_token),
    path(r'auth/token-verify/', verify_jwt_token),
    url(r'api/player/(?P<pk>[0-9]+)$', views.PlayerAPIView.as_view()),
    path(r'api/scenario', views.ScenarioListAPIView.as_view(), name='scenario-list'),
    path(r'api/question', views.QuestionListAPIView.as_view(), name='question-list'),
    url(r'^api/scenario/(?P<scenario>[0-9]+)/question/(?P<question>[0-9]+)/answer/(?P<answer>[0-9]+)$', views.AnswerAPIView.as_view(), name='answer-list'),
    url(r'^api/scenario/(?P<scenario>[0-9]+)/question/(?P<question>[0-9]+)/answers$', views.AnswerListAPIView.as_view()),
    url(r'^api/scenario/(?P<scenario>[0-9]+)/question/(?P<question>[0-9]+)$', views.QuestionAPIView.as_view()),
]