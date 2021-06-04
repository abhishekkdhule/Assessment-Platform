from django.urls import path
from .views import recruitersPage,questionsPage,createAssessment

urlpatterns = [
    path('',recruitersPage,name='recruiter'),
    path('newassm/<int:assgK>',createAssessment,name='newassm'),
    path('quetions/<int:assgK>',questionsPage,name='questions'),
    
]
