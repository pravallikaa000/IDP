# Generated by Django 5.0.1 on 2024-02-15 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_timetableentry_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetableentry',
            name='department',
        ),
    ]
