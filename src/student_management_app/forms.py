from django import forms
from student_management_app.models import Course

class DateInput(forms.DateInput):
    input_type="date"

class AddStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="User Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

    courses=Course.objects.all()
    course_list=[]
    for course in courses:
        p=(course.id,course.course_name)
        course_list.append(p)
    course=forms.ChoiceField(label="Courses",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
    Gender=(
        ("Male","Male"),
        ("Female","Female")
    )
    sex=forms.ChoiceField(label="Sex",choices=Gender,widget=forms.Select(attrs={"class":"form-control"}))
    session_start=forms.DateField(label="Session Start",widget=DateInput(attrs={"class":"form-control"}))
    session_end=forms.DateField(label="Session End",widget=DateInput(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Picture",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))



class EditStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="User Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

    courses=Course.objects.all()
    course_list=[]
    for course in courses:
        p=(course.id,course.course_name)
        course_list.append(p)
    course=forms.ChoiceField(label="Courses",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
    Gender=(
        ("Male","Male"),
        ("Female","Female")
    )
    sex=forms.ChoiceField(label="Sex",choices=Gender,widget=forms.Select(attrs={"class":"form-control"}))
    session_start=forms.DateField(label="Session Start",widget=DateInput(attrs={"class":"form-control"}))
    session_end=forms.DateField(label="Session End",widget=DateInput(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Picture",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}),required=False)