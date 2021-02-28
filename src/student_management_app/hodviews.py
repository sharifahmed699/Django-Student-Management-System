from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student_management_app.models import CustomUser, Staff,Course,Student,Subject


def admin_home(request):
    return render(request,"hod_template/home_content.html")

def add_staff(request):
    return render(request,"hod_template/add_staff.html")


def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.staff.address=address
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect(reverse("add_staff"))



def add_course(request):
    return render(request,"hod_template/add_course.html")


def add_course_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        course=request.POST.get("course")
        try:
            course_model=Course(course_name=course)
            course_model.save()
            messages.success(request,"Successfully Added Course")
            return HttpResponseRedirect(reverse("add_course"))
        except:
            messages.error(request,"Failed to Add Course")
            return HttpResponseRedirect(reverse("add_course"))


def add_student(request):
    course=Course.objects.all()
    return render(request,"hod_template/add_student.html",{"course":course})


def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
       
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        session_start=request.POST.get("session_start")
        session_end=request.POST.get("session_end")
        course_id=request.POST.get("course_id")
        sex=request.POST.get("sex")

        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
            user.student.address=address
            course_obj=Course.objects.get(id=course_id)
            user.student.course_id=course_obj
            user.student.session_start_year=session_start
            user.student.session_end_year=session_end
            user.student.gender=sex
            user.student.profile_pic=" "
            user.save()
            messages.success(request,"Successfully Added Student")
            return HttpResponseRedirect(reverse("add_student"))
        except:
            messages.error(request,"Failed to Add Student")
            return HttpResponseRedirect(reverse("add_student"))


def add_subject(request):
    course=Course.objects.all()
    staff=CustomUser.objects.filter(user_type=2)
    return render(request,"hod_template/add_subject.html",{"staff":staff,"course":course})

def add_subject_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_name=request.POST.get("subject_name")
        course_id=request.POST.get("course")
        course=Course.objects.get(id=course_id)
        staff_id=request.POST.get("staff")
        staff=CustomUser.objects.get(id=staff_id)

        try:
            subject=Subject(subject_name=subject_name,course_id=course,staff_id=staff)
            subject.save()
            messages.success(request,"Successfully Added Subject")
            return HttpResponseRedirect(reverse("add_subject"))
        except:
            messages.error(request,"Failed to Add Subject")
            return HttpResponseRedirect(reverse("add_subject"))


def manage_staff(request):
    staff=Staff.objects.all()
    return render(request,"hod_template/manage_staff.html",{"staff":staff})


def manage_student(request):
    student=Student.objects.all()
    return render(request,"hod_template/manage_student.html",{"student":student})

def manage_course(request):
    course=Course.objects.all()
    return render(request,"hod_template/manage_course.html",{"course":course})

def manage_subject(request):
    subject=Subject.objects.all()
    return render(request,"hod_template/manage_subject.html",{"subject":subject})