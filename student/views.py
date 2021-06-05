from django.shortcuts import render
from user.models import User
from assessment.models import AssessmentScore
# Create your views here.
def studentPage(request):
    assessments=AssessmentScore.objects.filter(user=request.user)
    print(assessments)
    context={
        "assessments":assessments
    }
    return render(request,'student/student.html',context=context)