from django.urls import path
from app1.views import *
app_name='csk'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
]