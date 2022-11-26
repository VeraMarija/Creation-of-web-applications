from .models import Korisnik
from django.shortcuts import redirect


def admin_required(function):
    def wrap(*args, **kwargs):
        if args[0].user.is_superuser:
            return function(*args, **kwargs)
        else:
            return redirect('login')
    return wrap


def mentor_required(function):
    def wrap(*args, **kwargs):
        if args[0].user.role == 'prof':
            return function(*args, **kwargs)
        else:
            return redirect('login')
    return wrap


def student_required(function):
    def wrap(*args, **kwargs):
        if args[0].user.role == 'stu':
            return function(*args, **kwargs)
        else:
            return redirect('login')
    return wrap
