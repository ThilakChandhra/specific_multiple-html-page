from app2.views import *
from django.urls import path

app_name='nothing'

urlpatterns=[
    path('third/',third,name='third'),
    path('fourth/',fourth,name='fourth'),
]