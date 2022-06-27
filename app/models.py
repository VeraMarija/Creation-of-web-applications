from secrets import choice
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Korisnik(AbstractUser):
    ROLES = (('prof', 'profesor'), ('stu', 'student'))
    STATUS = (('none', 'None'), ('izv', 'izvanredni student'),
              ('red', 'redovni student'))
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLES)
    status = models.CharField(max_length=50, choices=STATUS)

    ''' def __str__(self):
        return "%s" % (self.username)'''


class Course(models.Model):
    name = models.CharField(max_length=100)
    kod = models.CharField(max_length=50)
    program = models.CharField(max_length=100)
    ects = models.IntegerField()
    sem_red = models.IntegerField()
    sem_izv = models.IntegerField()
    IZBORNI = (('da', 'DA'), ('ne', 'NE'))
    izborni = models.CharField(max_length=50, choices=IZBORNI)
    nositelj_kolegija = models.ForeignKey(
        Korisnik, on_delete=models.CASCADE, blank=True, null=True)


class Upisni_list(models.Model):
    STATUS = (('enr', 'enrolled'), ('pass', 'passed'))
    korisnik = models.ForeignKey(
        Korisnik, on_delete=models.CASCADE, blank=True, null=True)
    predmet = models.ForeignKey(
        Course, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS)
