from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.signIn , name = 'signIn'),
    path('chatt',views.chat, name = 'chatt'),
    path('addqna',views.addqna, name = 'addqna'),
    path('fromexcel',views.llm , name = 'fromExcel'),
    path('contact',views.facebook , name = 'contact'),
    path('login',views.signIn , name = 'login'),
    path('reports',views.qna , name = 'reports'),



]

