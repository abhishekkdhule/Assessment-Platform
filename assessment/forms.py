from . models import Question
from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        exclude=['assessment']
        widgets={
            # 'assessment':forms.HiddenInput(),
            'question':forms.Textarea(attrs={'rows':2,'class':'form-control',"value":"random"}),
            'option_a':forms.TextInput(attrs={'class':'form-control mt-1'}),
            'option_b':forms.TextInput(attrs={'class':'form-control'}),
            'option_c':forms.TextInput(attrs={'class':'form-control'}),
            'option_d':forms.TextInput(attrs={'class':'form-control'}),
            'marks_assigned':forms.NumberInput(attrs={'class':'form-control mt-1'}),
            'correct_choice':forms.Select(attrs={'class':'form-select'}),

        }   
    