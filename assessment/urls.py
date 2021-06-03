from django.urls import path
from .views import recruitersPage,questionsPage

urlpatterns = [
    path('',recruitersPage,name='recruiter'),
    path('quetions/<int:assgK>',questionsPage,name='questions'),
    
]
