from django.urls import path
from app2.views import *
app_name='mi'
urlpatterns=[
    path('rohit/',rohit,name='rohit'),
]