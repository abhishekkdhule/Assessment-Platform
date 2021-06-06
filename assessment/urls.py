from django.urls import path
from .views import recruitersPage,questionsPage,createAssessment,assignToStudents,deleteAssessment,responsesOfAssessment

urlpatterns = [
    path('',recruitersPage,name='recruiter'),
    path('newassm/<int:assgK>',createAssessment,name='newassm'),
    path('delete/<int:assgK>',deleteAssessment,name='delete'),
    path('quetions/<int:assgK>',questionsPage,name='questions'),
    path('assign/<int:assgK>',assignToStudents,name='assign'),
    path('reponses/<int:assgK>',responsesOfAssessment,name='responses'),
]
