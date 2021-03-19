from django import forms
from django.forms import ModelForm

from .models import *

# this creates a form for each model in the models.py
class TaskForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

	class Meta:
		model = Task
		fields = '__all__'