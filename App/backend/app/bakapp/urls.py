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
    path(r'api/competences', views.CompetenceAPIView.as_view(), name='competence-list'),
    path(r'api/player', views.PlayerListAPIView.as_view()),
    path(r'api/roles', views.RoleAPIView.as_view(), name='role-list'),
    path(r'auth/', include('rest_auth.urls')),
    path(r'auth/registration/', include('rest_auth.registration.urls')),
    path(r'auth/token/', obtain_jwt_token),
    path(r'auth/token-refresh/', refresh_jwt_token),
    path(r'auth/token-verify/', verify_jwt_token),
    url(r'api/player/(?P<pk>[0-9]+)$', views.PlayerAPIView.as_view()),
]
