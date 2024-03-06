from django import forms
from .models import Todo

class CreateTodoForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=100, required=True)
    description = forms.CharField(min_length=0, max_length=255, required=False)
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    status = forms.BooleanField(required=False)


