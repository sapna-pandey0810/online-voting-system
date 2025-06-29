from django import forms
from django.contrib.auth.models import User
from .models import Vote, Candidate

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['candidate']
        widgets = {'candidate': forms.RadioSelect}
