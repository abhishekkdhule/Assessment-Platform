from django.urls import path
from .views import studentPage

urlpatterns = [
    path('',studentPage,name='student'),
]
