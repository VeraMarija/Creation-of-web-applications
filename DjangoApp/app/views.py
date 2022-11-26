from asyncio.log import logger
from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from .models import Korisnik, Course, Upisni_list
from .forms import CourseForm, StudentForm, MentorForm, upisniListForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .decorators import admin_required, mentor_required, student_required
# Create your views here.


# Trenutni korisnik u bazi
def logged_user(request):
    current_user = request.user
    return current_user

# Početna stranica za korisnika


@login_required
def home_page(request):
    user = logged_user(request)
    if user.is_superuser:
        return render(request, 'home_page_admin.html', {'admin': user})
    elif user.role == 'stu':
        return render(request, 'home_page_student.html', {'student': user})
    elif user.role == 'prof':
        return render(request, 'home_page_mentor.html', {'profesor': user})
    else:
        return HttpResponseNotAllowed


# -------------FUNKCIJE ZA ADMIN STRANICU-------------------------------------

# lista svih predmeta
@admin_required
def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses_list.html', {'data': courses})


# dodavanje novog predmeta od strane admina i mentora
@admin_required
def add_new_course(request):
    if request.method == "GET":
        courseForm = CourseForm()
        return render(request, 'add_course.html', {'form': courseForm.as_table()})
    elif request.method == "POST":
        courseForm = CourseForm(request.POST)
        if courseForm.is_valid():
            courseForm.save()
            return redirect('courses')
        else:
            return HttpResponse('form not valid!')
    return redirect('courses')


@admin_required
def edit_course(request, course_id):
    course_by_id = Course.objects.get(id=course_id)
    if request.method == "GET":
        courseForm = CourseForm(instance=course_by_id)
        return render(request, 'edit_course.html', {'form': courseForm.as_table()})
    elif request.method == "POST":
        courseForm = CourseForm(request.POST, instance=course_by_id)
        if courseForm.is_valid():
            courseForm.save()
            return redirect('courses')
        else:
            return HttpResponse('form not valid!')
    return redirect('courses')


@admin_required
def details_course(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'details_course.html', {'data': course})


@admin_required
def students_on_course(request, course_id):
    students_ids = Upisni_list.objects.filter(
        predmet_id=course_id).values_list('korisnik_id', flat=True)
    list = []
    for id in students_ids:
        list.append(Korisnik.objects.get(pk=id))
    return render(request, 'students_on_course.html', {'data': list})


@admin_required
def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'GET':
        return render(request, 'delete_course.html', {'data': course})
    elif request.method == "POST":
        if 'DA' in request.POST:
            course.delete()
            return redirect('courses')
        else:
            return redirect('courses')
    else:
        return HttpResponse("you can't delete the course you are not admin!")


@admin_required
def students_list(request):
    students = Korisnik.objects.filter(role='stu')
    return render(request, 'students_list.html', {'data': students})


@admin_required
def add_new_student(request):
    if request.POST:
        studentForm = StudentForm(request.POST)
        if studentForm.is_valid():
            studentForm.role = 'stu'
            studentForm.save()
            email = studentForm.cleaned_data.get("email")
            raw_password = studentForm.cleaned_data.get("password1")
            return redirect('students')
        else:
            return HttpResponse(studentForm.errors)
    else:
        studentForm = StudentForm()
    return render(request, 'add_student.html', {'form': studentForm.as_table()})


@admin_required
def edit_student(request, student_id):
    student_by_id = Korisnik.objects.get(id=student_id)
    if request.method == "GET":
        studentForm = StudentForm(instance=student_by_id)
        return render(request, 'edit_student.html', {'form': studentForm.as_table()})
    elif request.method == "POST":
        studentForm = StudentForm(request.POST, instance=student_by_id)
        if studentForm.is_valid():
            studentForm.save()
            return redirect('students')
        else:
            return HttpResponse('form not valid!')
    return redirect('students')


@admin_required
def details_student(request, student_id):
    student = Korisnik.objects.get(id=student_id)
    return render(request, 'details_student.html', {'data': student})


@admin_required
def delete_student(request, student_id):
    student = Korisnik.objects.get(id=student_id)
    if request.method == 'GET':
        return render(request, 'delete_student.html', {'data': student})
    elif request.method == "POST":
        if 'DA' in request.POST:
            student.delete()
            return redirect('students')
        else:
            return redirect('students')
    else:
        return HttpResponse("you can't delete the student you are not admin!")


@admin_required
def delete_mentor(request, mentor_id):
    mentor = Korisnik.objects.get(id=mentor_id)
    if request.method == 'GET':
        return render(request, 'delete_mentor.html', {'data': mentor})
    elif request.method == "POST":
        if 'DA' in request.POST:
            mentor.delete()
            return redirect('mentors')
        else:
            return redirect('mentors')
    else:
        return HttpResponse("you can't delete the mentor you are not admin!")


@admin_required
def mentors_list(request):
    mentors = Korisnik.objects.filter(role='prof')
    return render(request, 'mentors_list.html', {'data': mentors})


@admin_required
def add_new_mentor(request):
    if request.POST:
        mentorForm = MentorForm(request.POST)
        if mentorForm .is_valid():
            mentorForm .save()
            email = mentorForm .cleaned_data.get("email")
            raw_password = mentorForm .cleaned_data.get("password1")
            return redirect('mentors')
        else:
            return HttpResponse(mentorForm.errors)
    else:
        mentorForm = MentorForm()
    return render(request, 'add_mentor.html', {'form': mentorForm.as_table()})


@admin_required
def edit_mentor(request, mentor_id):
    mentor_by_id = Korisnik.objects.get(id=mentor_id)
    if request.method == "GET":
        mentorForm = MentorForm(instance=mentor_by_id)
        return render(request, 'edit_student.html', {'form': mentorForm.as_table()})
    elif request.method == "POST":
        mentorForm = MentorForm(request.POST, instance=mentor_by_id)
        if mentorForm.is_valid():
            mentorForm.save()
            return redirect('mentors')
        else:
            return HttpResponse(mentorForm.errors)
    return redirect('mentors')


@admin_required
def details_mentor(request, mentor_id):
    mentor = Korisnik.objects.get(id=mentor_id)
    return render(request, 'details_mentor.html', {'data': mentor})


# -------------FUNKCIJE ZAJEDNICKE-------------------------------------


@login_required
def upisni_list(request, student_id):
    student = Korisnik.objects.get(id=student_id)
    status_studenta = student.status
    all_courses_ids = Upisni_list.objects.filter(
        korisnik_id=student_id).values_list('predmet_id', flat=True)
    neupisani_predmeti = Course.objects.all()
    for i in all_courses_ids:  # izbacivanje onih id koji su vec u all_courses_ids
        neupisani_predmeti = neupisani_predmeti.filter(~Q(id=i))
    dict = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
    if status_studenta == 'izv':
        for key, value in dict.items():
            for id in all_courses_ids:
                if key == Course.objects.get(pk=id).sem_izv:
                    dict[key].append({Course.objects.get(pk=id): Upisni_list.objects.filter(
                        korisnik_id=student_id).get(predmet_id=id)})
    else:
        for key, value in dict.items():
            for id in all_courses_ids:
                if key == Course.objects.get(pk=id).sem_red:
                    dict[key].append({Course.objects.get(pk=id): Upisni_list.objects.filter(
                        korisnik_id=student_id).get(predmet_id=id)})

    # u svakom value od dicta za semestar je lista predmeta u tom semestru
    list = [dict[1], dict[2], dict[3], dict[4],
            dict[5], dict[6], dict[7], dict[8]]
    if status_studenta == 'red':
        list.remove(dict[7])
        list.remove(dict[8])

    if request.user.is_superuser:
        return render(request, 'upisni_admina.html', {'neupisani_predmeti': neupisani_predmeti, 'id': student.id, 'email': student.email, 'semesters': list})
    elif request.user.role == 'stu':
        return render(request, 'upisni_studenta.html', {'neupisani_predmeti': neupisani_predmeti, 'id': student.id, 'email': student.email, 'semesters': list})
    else:
        list = upisni_profesora(request, student_id)
        return render(request, 'upisni_profesora.html', {'id': student.id, 'email': student.email, 'semesters': list})


@login_required
def add_course_to_upisni(request, student_id, course_id):
    new_upisni = Upisni_list(
        korisnik=Korisnik.objects.get(id=student_id), predmet=Course.objects.get(id=course_id), status='enr')
    new_upisni.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def promijeni_status(request, upisni_id):
    if Upisni_list.objects.get(id=upisni_id).status == 'enr':
        Upisni_list.objects.filter(id=upisni_id).update(status='pass')
    else:
        Upisni_list.objects.filter(id=upisni_id).update(status='enr')
    return redirect(request.META.get('HTTP_REFERER'))


# -------------FUNKCIJE ZA MENTOR STRANICU-------------------------------------

# - pregled liste predmeta prijavljenog profesora
@mentor_required
def mentor_courses(request):
    user = request.user
    all_mentor_courses = Course.objects.filter(nositelj_kolegija=user.id)
    return render(request, "mentor_courses.html", {'data': all_mentor_courses})

# - pregled popisa studenata na pojedinom kolegiju (kojem je prijavljeni profesor nositelj)


@mentor_required
def students_on_mentor_course(request, course_id):
    course = Course.objects.get(id=course_id)
    students_ids = Upisni_list.objects.filter(
        predmet_id=course_id).values_list('korisnik', flat=True)
    korisnici = Korisnik.objects.all()
    list = []
    for i in students_ids:
        if Korisnik.objects.get(id=i):
            list.append(Korisnik.objects.get(id=i))
    return render(request, "mentor_students.html", {'data': list, 'kolegij': course})


# - mijenjanje statusa predmeta (po defaultu je samo upisan, a moze se promijeniti u
# „polozen” ili „izgubio potpis”. Predmet se moze ispisati sve dok mu status nije promijenjen
# u polozen/izgubio potpis)
@login_required
def upisni_profesora(request, student_id):
    predmeti_profesora = Course.objects.filter(
        nositelj_kolegija=request.user.id)
    student = Korisnik.objects.get(id=student_id)
    status_studenta = student.status
    all_courses_ids = Upisni_list.objects.filter(
        korisnik_id=student_id).values_list('predmet_id', flat=True)
    predmeti = []
    for i in all_courses_ids:
        for p in predmeti_profesora:
            if p.id == i:
                predmeti.append(p)
    dict = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
    if status_studenta == 'izv':
        for key, value in dict.items():
            for i in predmeti:
                if key == Course.objects.get(pk=i.id).sem_izv:
                    dict[key].append({Course.objects.get(pk=i.id): Upisni_list.objects.filter(
                        korisnik_id=student_id).get(predmet_id=i.id)})
    else:
        for key, value in dict.items():
            for i in predmeti:
                if key == Course.objects.get(pk=i.id).sem_red:
                    dict[key].append({Course.objects.get(pk=i.id): Upisni_list.objects.filter(
                        korisnik_id=student_id).get(predmet_id=i.id)})
    list = [dict[1], dict[2], dict[3], dict[4],
            dict[5], dict[6], dict[7], dict[8]]
    if status_studenta == 'red':
        list.remove(dict[7])
        list.remove(dict[8])
    return list


# pregled studenata na svakom pojedinom predmetu prema sljedecim kriterijima:
# 3. studenti koji su polozili predmet
@mentor_required
def studenti_polozili(request, course_id):
    polozeni = Upisni_list.objects.filter(
        predmet_id=course_id).filter(status='pass').values_list('korisnik', flat=True)
    list = []
    for i in polozeni:
        list.append(Korisnik.objects.get(id=i))
    return render(request, 'studenti_polozili.html', {'studenti': list, 'kolegij': Course.objects.get(id=course_id)})


# -------------FUNKCIJE ZA STUDENT STRANICU-------------------------------------
# brisanje predmeta s upisnog
@student_required
def ispisi_predmet(request, student_id, course_id):
    upisni = Upisni_list.objects.filter(korisnik_id=student_id).filter(
        predmet_id=course_id).values_list('pk', flat=True)
    polozeni = Upisni_list.objects.filter(
        predmet_id=course_id).filter(status='pass').values_list('korisnik', flat=True)
    Upisni_list.objects.get(id=upisni[0]).delete()
    return redirect(request.META.get('HTTP_REFERER'))
