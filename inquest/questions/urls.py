from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'questions'

urlpatterns = [

    path('', views.questions_home, name='questions_home'),
    path('<str:questions_id>/', views.details, name='details')

]
