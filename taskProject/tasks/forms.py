from django import forms
from .models import Task, TimeEntry

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

class TimeEntryForm(forms.ModelForm):
    class Meta:
        model = TimeEntry
        fields = "__all__"