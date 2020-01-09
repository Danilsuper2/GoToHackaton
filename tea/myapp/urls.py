from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('test/', views.test),
    path('tea/', views.tea),
    path('time_and_place/', views.time_and_place)
]