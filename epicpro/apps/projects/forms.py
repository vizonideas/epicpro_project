#encoding:utf-8
from django.forms import ModelForm
from django import forms

from .models import Team, Member

from django.contrib.auth.forms import UserCreationForm

class RegisterUserTeamForm(UserCreationForm):
	team = forms.CharField(max_length=100)


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ('name','resumen',)


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ('team','user','state','can_create_project',)