from django.db import models
from user.models import User


class Assessment(models.Model):
    title=models.CharField(max_length=200)
    createdBy=models.ForeignKey(User,on_delete=models.CASCADE)
    createdOn=models.DateTimeField(auto_now_add=True)
    max_score=models.DecimalField(max_digits=6,decimal_places=2,default=0.0)

    def __str__(self):
        return self.title


class Question(models.Model):
    answer_choice = [
        ('a', 'option a'),
        ('b', 'option b'),
        ('c', 'option c'),
        ('d', 'option d'),
    ]
    assessment=models.ForeignKey(Assessment,on_delete=models.CASCADE)
    question=models.CharField(max_length=500)
    option_a=models.CharField(max_length=300)
    option_b=models.CharField(max_length=300)
    option_c=models.CharField(max_length=300)
    option_d=models.CharField(max_length=300)
    marks_assigned=models.DecimalField(max_digits=4,decimal_places=2)
    correct_choice=models.CharField(max_length=1,choices=answer_choice,default='a')

    def __str__(self):
        return "A"+str(self.assessment.id)


class AssessmentScore(models.Model):
    assessment=models.ForeignKey(Assessment,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_pending=models.BooleanField(default=False)
    score_obtained=models.DecimalField(max_digits=6,decimal_places=2,default=0.0)

    def __str__(self):
        return "A"+str(self.assessment.id)+" U"+str(self.user.id)
    
    