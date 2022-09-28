from django import forms
from django import forms
from todolist.models import Task

class FormTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = {"title", "description"}