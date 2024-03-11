from django.contrib import admin

from .models import Faculty,Course,Section,TimetableEntry

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(TimetableEntry)