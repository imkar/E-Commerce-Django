from django import forms
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(label=False,max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username","action":"www.google.com"}))
    email = forms.EmailField(label=False,widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}))
    password = forms.CharField(label=False,widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(label=False,widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        return data



class LoginForm(forms.Form):
    username = forms.CharField(label=False,max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))
    password = forms.CharField(label=False,widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
