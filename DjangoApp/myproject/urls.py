"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('home/', views.home_page, name='home_page'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('courses/', views.courses_list, name='courses'),
    path('students/', views.students_list, name='students'),
    path('mentors/', views.mentors_list, name='mentors'),
    path('new_course/', views.add_new_course, name='new_course'),
    path('edit_course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('details_course/<int:course_id>/',
         views.details_course, name='details_course'),
    path('students_list/<int:course_id>/',
         views.students_on_course, name='students_list'),
    path('delete_course/<int:course_id>/',
         views.delete_course, name='delete_course'),
    path('new_student/', views.add_new_student, name='new_student'),
    path('edit_student/<int:student_id>/',
         views.edit_student, name='edit_student'),
    path('details_student/<int:student_id>/',
         views.details_student, name='details_student'),
    path('upisni_studenta/<int:student_id>/',
         views.upisni_list, name='upisni_studenta'),
    path('delete_student/<int:student_id>/',
         views.delete_student, name='delete_student'),
    path('delete_mentor/<int:mentor_id>/',
         views.delete_mentor, name='delete_mentor'),
    path('new_mentor/', views.add_new_mentor, name='new_mentor'),
    path('edit_mentor/<int:mentor_id>/',
         views.edit_mentor, name='edit_mentor'),
    path('details_mentor/<int:mentor_id>/',
         views.details_mentor, name='details_mentor'),
    path('upisni_admina/<int:student_id>/',
         views.upisni_list, name='upisni_admina'),
    path('upisni_profesora/<int:student_id>/',
         views.upisni_list, name='upisni_profesora'),
    path('add_course_to_upisni/<int:student_id>/<int:course_id>/',
         views.add_course_to_upisni, name='add_course_to_upisni'),
    path('promijeni_status/<int:upisni_id>/',
         views.promijeni_status, name='promijeni_status'),
    path('mentor_courses/',
         views.mentor_courses, name='mentor_courses'),
    path('kolegij_studenti/<int:course_id>/',
         views.students_on_mentor_course, name='kolegij_studenti'),
    path('studenti_polozili/<int:course_id>/',
         views.studenti_polozili, name='studenti_polozili'),
    path('ispisi_predmet/<int:student_id>/<int:course_id>/',
         views.ispisi_predmet, name='ispisi_predmet'),


]
