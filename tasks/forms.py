from django import forms
from .models import Task


class Create_Task_Forms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']


class Update_Task_Forms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

        