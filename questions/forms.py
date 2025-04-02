from django import forms
from .models import Message

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body': forms.HiddenInput(), 
        }
        labels = {
            'body': 'Your Question',
        }