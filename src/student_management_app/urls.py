from django.urls import path,include
#from . import views
#from student_management_app.hodviews import admin_home
#from . import hodviews
from student_management_app import views, hodviews,StaffView,StudentView

urlpatterns = [
    path('demu',views.Index,name="index"),
    path('',views.ShowLoginPage,name="login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),
    path('admin_home',hodviews.admin_home,name="admin_home"),
    path('add_staff',hodviews.add_staff,name="add_staff"),
    path('add_staff_save',hodviews.add_staff_save,name="add_staff_save"),
    path('add_course',hodviews.add_course,name="add_course"),
    path('add_course_save',hodviews.add_course_save,name="add_course_save"),
    path('add_student',hodviews.add_student,name="add_student"),
    path('add_student_save',hodviews.add_student_save,name="add_student_save"),
    path('add_subject',hodviews.add_subject,name="add_subject"),
    path('add_subject_save',hodviews.add_subject_save,name="add_subject_save"),
    path('manage_staff',hodviews.manage_staff,name="manage_staff"),
    path('manage_student',hodviews.manage_student,name="manage_student"),
    path('manage_course',hodviews.manage_course,name="manage_course"),
    path('manage_subject',hodviews.manage_subject,name="manage_subject"),
    path('edit_staff/<str:staff_id>',hodviews.edit_staff,name="edit_staff"),
    path('edit_staff_save',hodviews.edit_staff_save,name="edit_staff_save"),
    path('edit_student/<str:student_id>',hodviews.edit_student,name="edit_student"),
    path('edit_student_save',hodviews.edit_student_save,name="edit_student_save"),
    path('edit_subject/<str:subject_id>',hodviews.edit_subject,name="edit_subject"),
    path('edit_subject_save',hodviews.edit_subject_save,name="edit_subject_save"),
    path('edit_course/<str:course_id>',hodviews.edit_course,name="edit_course"),
    path('edit_course_save',hodviews.edit_course_save,name="edit_course_save"),
    
    path('student_home', StudentView.student_home, name="student_home"),
    path('manage_session', hodviews.manage_session,name="manage_session"),
    path('add_session_save', hodviews.add_session_save,name="add_session_save"),

    path('staff_home', StaffView.staff_home, name="staff_home"),
    path('staff_take_attendance', StaffView.staff_take_attendance,name="staff_take_attendance"),
    path('get_students', StaffView.get_students, name="get_students"),
       path('save_attendance_data', StaffView.save_attendance_data, name="save_attendance_data"),
    
    
] 


