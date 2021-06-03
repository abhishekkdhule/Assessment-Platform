from django.shortcuts import render
from . models import Assessment,Question,AssessmentScore
from . forms import QuestionForm
# Create your views here.

def recruitersPage(request):
    
    assessments=Assessment.objects.filter(createdBy=request.user)
    return render(request,'assessment/recruiter.html',context={"assessments":assessments})

def questionsPage(request,assgK):
    form=QuestionForm()
    assessment=Assessment.objects.get(id=assgK)
    questions=Question.objects.filter(assessment=assessment)
    return render(request,'assessment/que.html',{"questions":questions,"form":form})

def createAssessment(request,assgK):
    pass