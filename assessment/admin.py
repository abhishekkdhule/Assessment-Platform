from django.contrib import admin
from . models import Assessment,Question,AssessmentScore


admin.site.register(AssessmentScore)
admin.site.register(Assessment)
admin.site.register(Question)
