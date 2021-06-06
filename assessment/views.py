from django.shortcuts import render,redirect
from django.http import Http404
from . models import Assessment,Question,AssessmentScore
from . forms import QuestionForm
from user.models import User


#Homepage of recruiter
def recruitersPage(request):
    if request.method=="POST":
        assessmentTitle=request.POST['assessment']
        assmObj=Assessment.objects.create(title=assessmentTitle,createdBy=request.user)
        return redirect('newassm',assmObj.id)
    assessments=Assessment.objects.filter(createdBy=request.user)
    return render(request,'assessment/recruiter.html',context={"assessments":assessments})

#Creation of new assessment
def createAssessment(request,assgK):
    assmObj=Assessment.objects.get(id=assgK)
    if assmObj.createdBy==request.user:
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
    raise Http404()

#Assigning  assessment to students
def assignToStudents(request,assgK):
    assessment=Assessment.objects.get(id=assgK)
    if(assessment.createdBy==request.user):
        for key,val in dict(request.POST).items():
            try:
                userid=(int(val[0]))
            except:
                continue
            assgObj=Assessment.objects.get(id=assgK)
            userObj=User.objects.get(id=userid)
            AssessmentScore.objects.create(assessment=assgObj,user=userObj)
        return redirect('newassm',assgK)
    raise Http404()

#To view questions of an assessment
def questionsPage(request,assgK):
    assessment=Assessment.objects.get(id=assgK)
    if(assessment.createdBy==request.user):
        questions=Question.objects.filter(assessment=assessment)
        return render(request,'assessment/que.html',{"questions":questions,"assessment":assessment})
    raise Http404()

#View for deleting assessments
def deleteAssessment(request,assgK):
    assgObj=Assessment.objects.get(id=assgK)
    if(assgObj.createdBy==request.user):
        assgObj.delete()
        return redirect('recruiter')
    raise Http404()

#View responses of particular Assessment
def responsesOfAssessment(request,assgK):
    assgObj=Assessment.objects.get(id=assgK)
    if(assgObj.createdBy==request.user):
        responses=AssessmentScore.objects.filter(assessment=assgObj)
        context={
            "responses":responses
        }
        return render(request,'assessment/responses.html',context)
    raise Http404()

