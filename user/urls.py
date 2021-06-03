from django.urls import path
from . views import login,register,logout,recruitersPage,studentsPage

urlpatterns = [
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('logout/',logout,name='logout'),
    path('recruiter/',recruitersPage,name='recruiter'),
    path('student/',studentsPage,name='student'),
    
]
