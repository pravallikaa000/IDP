# Generated by Django 5.0.1 on 2024-02-24 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_remove_course_faculties_remove_faculty_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='courses',
        ),
    ]
