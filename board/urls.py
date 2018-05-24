from django.urls import path
from . import views


urlpatterns=[
    path('', views.bulletin_list, name='bulletin_list'),
]