from django.forms import ModelForm
from django import forms
from .models import schedule
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ScheduleForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ScheduleForm, self).__init__(*args, **kwargs)
		
		self.fields['date'].widget.attrs.update(
            {'placeholder': 'yyyy-mm-dd',})
	class Meta:
		model = schedule
		fields = ['fullname', 'purpose', 'dept', 'date', 'category']
class StatusForm(ModelForm):
	class Meta:
		model = schedule
		fields = ['status']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']