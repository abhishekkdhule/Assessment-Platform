from django.shortcuts import render,redirect
from user.models import User
from assessment.models import AssessmentScore
from assessment.models import Question,Assessment,AssessmentScore
from django.http import Http404

# This is a hompage of student
def studentPage(request):
    pendingAssessment=(AssessmentScore.objects.filter(user=request.user)).filter(is_pending=True)
    completedAssessment=(AssessmentScore.objects.filter(user=request.user)).filter(is_pending=False)
    context={
        "pendingAssessment":pendingAssessment,
        "completedAssessment":completedAssessment,
    }
    return render(request,'student/student.html',context=context)

# This is a assessment page of student
def studentsAssessment(request,assgK):
    assgObj=Assessment.objects.get(id=assgK)
    questions=Question.objects.filter(assessment=assgObj)
    try:
        assgScoreObj=(AssessmentScore.objects.filter(user=request.user)).get(assessment=assgObj)
        if request.method=="POST":
            totalScore=0
            for que in questions:
                if(request.POST[str(que.id)]==que.correct_choice):
                    totalScore+=que.marks_assigned
            assgScoreObj.is_pending=False
            assgScoreObj.score_obtained=totalScore
            assgScoreObj.save()
            return redirect('student')
        context={
            "questions":questions,
            "assessment":assgObj
        }
        return render(request,'student/assessment.html',context)
    except:
        raise Http404