import json
from datetime import datetime
from uuid import uuid4

from django.contrib import messages
from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from student_management_app.models import Subject, SessionYearModel, Student, Attendance, AttendanceReport, \
 Staff,  CustomUser, Course


def staff_home(request):
    return render(request,"staff_template/staff_home_template.html")


def staff_take_attendance(request):
    subjects=Subject.objects.filter(staff_id=request.user.id)
    session_years=SessionYearModel.object.all()
    return render(request,"staff_template/attendance.html",{"subjects":subjects,"session_years":session_years})


@csrf_exempt
def get_students(request):
    subject_id=request.POST.get("subject")
    session_year=request.POST.get("session_year")

    subject=Subject.objects.get(id=subject_id)
    session_model=SessionYearModel.object.get(id=session_year)
    students=Student.objects.filter(course_id=subject.course_id,session_year_id=session_model)
    list_data=[]

    for student in students:
        data_small={"id":student.admin.id,"name":student.admin.first_name+" "+student.admin.last_name}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)


@csrf_exempt
def save_attendance_data(request):
    student_ids=request.POST.get("student_ids")
    subject_id=request.POST.get("subject_id")
    attendance_date=request.POST.get("attendance_date")
    session_year_id=request.POST.get("session_year_id")

    subject_model=Subjects.objects.get(id=subject_id)
    session_model=SessionYearModel.object.get(id=session_year_id)
    json_sstudent=json.loads(student_ids)
    #print(data[0]['id'])


    try:
        attendance=Attendance(subject_id=subject_model,attendance_date=attendance_date,session_year_id=session_model)
        attendance.save()

        for stud in json_sstudent:
             student=Students.objects.get(admin=stud['id'])
             attendance_report=AttendanceReport(student_id=student,attendance_id=attendance,status=stud['status'])
             attendance_report.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("ERR")