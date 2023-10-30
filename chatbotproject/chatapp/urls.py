
from django.contrib import admin 
from django.urls import path 
from . import views


urlpatterns = [
    path('chatt',views.chat , name = 'chatt'),
    path('qnat',views.qna , name = 'qnat'),
    path('addqna',views.addqnat , name = 'addqna'),
]
