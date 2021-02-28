from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from student_management_app.models import CustomUser,Staff

# Register your models here.
admin.site.register(Staff)

class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)

