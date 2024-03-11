from django.urls import path
from . import views

urlpatterns = [
  path("",views.starting_page,name="starting-page"),
  path('home/',views.home_page,name="home-page"),
  path('home/admin1.html', views.admin1_page, name='admin1'),
  path('home/fac.html', views.fac_page, name='fac'),
  path('home/faculty.html', views.faculty_page, name='faculty'),
  path('home/student.html', views.student_page, name='student'),
  path('home/course.html', views.course_page, name='course'),
  path('home/section.html', views.section_page, name='section'),
  path('home/gentimetable.html', views.gentimetable_page, name='gentimetable'),
  path('home/viewcourse.html', views.viewcourse_page, name='viewcourse'),
  path('home/viewfaculty.html', views.viewfaculty_page, name='viewfaculty'),
]