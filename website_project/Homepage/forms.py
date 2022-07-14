from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Homepage.models import Register


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = Register
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
class RegForm(forms.Form):
		username=forms.CharField(max_length=255)
		email=forms.EmailField(max_length=255)
		password=forms.CharField(max_length=255)

class LoginForm(forms.Form):
	username = forms.CharField(max_length=255)
	password = forms.CharField(max_length=255)
	