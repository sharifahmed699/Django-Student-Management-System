# Generated by Django 3.1.6 on 2021-03-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0003_auto_20210303_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereportstudent',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
    ]
