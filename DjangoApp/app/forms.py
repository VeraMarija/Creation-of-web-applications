from dataclasses import field
from random import choices
from secrets import choice
from django import forms
from .models import Course, Korisnik, Upisni_list
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.forms import UserCreationForm


class CourseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields.get(
            'nositelj_kolegija').queryset = Korisnik.objects.filter(role='prof')

    class Meta:
        exclude = []
        model = Course


class StudentForm(UserCreationForm):
    ROLES = (('stu', 'student'),)
    STATUS = (('red', 'redovni student'), ('izv', 'izvanredni student')
              )
    email = forms.EmailField(max_length=100)
    role = forms.ChoiceField(choices=ROLES)
    status = forms.ChoiceField(choices=STATUS)

    class Meta:
        model = Korisnik
        fields = ("email", "username", "password1",
                  "password2", "role", "status")


class MentorForm(UserCreationForm):
    ROLES = (('prof', 'profesor'),)
    email = forms.EmailField(max_length=100)
    role = forms.ChoiceField(choices=ROLES)

    class Meta:
        model = Korisnik
        fields = ("email", "username", "password1",
                  "password2", "role", )


class upisniListForm(ModelForm):
    STATUS = (('enr', 'enrolled'),)
    status = forms.ChoiceField(choices=STATUS)

    class Meta:
        model = Upisni_list
        fields = ("korisnik", "predmet", "status")
