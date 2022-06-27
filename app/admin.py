from itertools import count
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Korisnik, Course, Upisni_list

# Register your models here.s
# admin.site.register(Korisnik)


@admin.register(Korisnik)
class KorisnikAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('None', {'fields': ('role', 'status')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('None', {'fields': ('role', 'status')}),
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Upisni_list)
class UpisiAdmin(admin.ModelAdmin):
    pass
