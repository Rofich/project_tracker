from django import forms
from .models import User, Project
from django.contrib.auth import authenticate, login


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')

    def save(self):
        data = self.cleaned_data
        user = User(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        user.set_password(data['password'])
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'end_time')
        widgets = {
            'end_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local'
            })
        }
        
    def save(self):
        model = Project()
        data = self.cleaned_data
        model.user = self.instance
        model.name = data['name']
        model.description = data['description']
        model.end_time = data['end_time']
        model.save()
        
        