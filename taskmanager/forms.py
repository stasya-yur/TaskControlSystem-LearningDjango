from django import forms
from .models import Task, Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'text', 'status', 'priority', 'deadline']
        widgets = {
            'deadline':forms.DateTimeInput(attrs={'type':'datetime-local'})
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
