from django.shortcuts import render,redirect
from . models import Assessment,Question,AssessmentScore
from . forms import QuestionForm
from user.models import User
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
    students=User.objects.filter(is_recruiter=False)
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
        "questions":ques,
        "students":students
    }
    return render(request,'assessment/newassm.html',context)


def assignToStudents(request,assgK):
    print(dict(request.POST))
    for key,val in dict(request.POST).items():
        try:
            userid=(int(val[0]))
        except:
            continue

        
        assgObj=Assessment.objects.get(id=assgK)
        userObj=User.objects.get(id=userid)
        AssessmentScore.objects.create(assessment=assgObj,user=userObj)
    return redirect('newassm',assgK)


def questionsPage(request,assgK):
    assessment=Assessment.objects.get(id=assgK)
    questions=Question.objects.filter(assessment=assessment)
    return render(request,'assessment/que.html',{"questions":questions,"assessment":assessment})

