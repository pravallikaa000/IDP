# Generated by Django 5.0.1 on 2024-02-15 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetableentry',
            name='day',
        ),
        migrations.RemoveField(
            model_name='timetableentry',
            name='time',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]
