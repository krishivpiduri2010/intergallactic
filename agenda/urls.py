from django.urls import path
from .views import home,create
urlpatterns=[
    path('',home,name='agenda_home'),
    path('create',create,name='agenda_create'),
]