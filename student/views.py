from django.shortcuts import render,redirect
from user.models import User
from assessment.models import AssessmentScore
from assessment.models import Question,Assessment,AssessmentScore

# This is a hompage of student
def studentPage(request):
    assessments=AssessmentScore.objects.filter(user=request.user)
    print(assessments)
    context={
        "assessments":assessments
    }
    return render(request,'student/student.html',context=context)

# This is a assessment page of student
def studentsAssessment(request,assgK):
    assgObj=Assessment.objects.get(id=assgK)
    questions=Question.objects.filter(assessment=assgObj)
    if request.method=="POST":
        totalScore=0
        assgScoreObj=(AssessmentScore.objects.filter(user=request.user)).get(assessment=assgObj)
        for que in questions:
            if(request.POST[str(que.id)]==que.correct_choice):
                totalScore+=que.marks_assigned
        assgScoreObj.is_pending=False
        assgScoreObj.score_obtained=totalScore
        assgScoreObj.save()
        print(request.POST)
        return redirect('student')
    context={
        "questions":questions,
        "assessment":assgObj
    }
    return render(request,'student/assessment.html',context)