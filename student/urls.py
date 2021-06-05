from django.urls import path
from .views import studentPage,studentsAssessment

urlpatterns = [
    path('',studentPage,name='student'),
    path('assessment/<int:assgK>/',studentsAssessment,name='quiz'),
]
