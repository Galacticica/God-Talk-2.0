from django import forms
from .models import Message

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body'] 
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Type your question here...',
                'class': 'form-control',
                'rows': 5,
            }),
        }
        labels = {
            'body': 'Your Question',
        }

