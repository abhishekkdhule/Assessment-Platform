from django.shortcuts import render,redirect
from . models import Assessment,Question,AssessmentScore
from . forms import QuestionForm
# Create your views here.

def recruitersPage(request):
    if request.method=="POST":
        print(request.POST)
        assessmentTitle=request.POST['assessment']
        assmObj=Assessment.objects.create(title=assessmentTitle,createdBy=request.user)
        print("assessment obj",assmObj)
        return redirect('newassm',assmObj.id)
    assessments=Assessment.objects.filter(createdBy=request.user)
    return render(request,'assessment/recruiter.html',context={"assessments":assessments})

def createAssessment(request,assgK):
    assmObj=Assessment.objects.get(id=assgK)
    ques=Question.objects.filter(assessment=assmObj)
    form=QuestionForm()
    if request.method=="POST":
        f=QuestionForm(request.POST)
        if(f.is_valid()):
            queObj=f.save(commit=False)   
            queObj.assessment=assmObj
            queObj.save() 
            assmObj.max_score+=queObj.marks_assigned
            assmObj.save()
            return redirect('newassm',assmObj.id)
    context={
        "assessment":assmObj,
        "form":form,
        "questions":ques
    }
    return render(request,'assessment/newassm.html',context)

def questionsPage(request,assgK):
    assessment=Assessment.objects.get(id=assgK)
    questions=Question.objects.filter(assessment=assessment)
    return render(request,'assessment/que.html',{"questions":questions,"assessment":assessment})

