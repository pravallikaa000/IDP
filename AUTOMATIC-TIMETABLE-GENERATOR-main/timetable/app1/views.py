from django.shortcuts import render, redirect
from .models import Course, Faculty
from .forms import CourseForm, FacultyForm


def starting_page(request):
    return render(request, "app1/main.html")

def home_page(request):
    return render(request, "app1/home.html")

def admin1_page(request):
    return render(request, 'app1/admin1.html')

def viewcourse_page(request):
    # Fetch all courses from the database
    courses = Course.objects.all()
    return render(request, 'app1/viewcourse.html', {"courses": courses})

def fac_page(request):
    return render(request, 'app1/fac.html')

def faculty_page(request):
    faculties = Faculty.objects.all()

    if request.method == 'POST':
        form = FacultyForm(request.POST)

        if form.is_valid():
            if 'addfaculty' in request.POST:
                faculty = form.save(commit=False)
                faculty.save()
                return redirect('viewfaculty')
    else:
        form = FacultyForm()

    return render(request, 'app1/faculty.html', {"form": form, "faculties": faculties})

def student_page(request):
    return render(request, 'app1/student.html')

def viewfaculty_page(request):
    faculties = Faculty.objects.all()
    return render(request, 'app1/viewfaculty.html', {"faculties": faculties})

def course_page(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            if 'addcourse' in request.POST:
                # Get the cleaned data from the form
                cleaned_data = form.cleaned_data
                
                # Create a new Course instance with the cleaned data
                course = Course(
                    cid=cleaned_data['course_id'],
                    cname=cleaned_data['course_name']
                )

                # Save the new course instance
                course.save()

                
    else:
        form = CourseForm()

    # Fetch all courses from the database
    courses = Course.objects.all()
    return render(request, 'app1/course.html', {"form": form, "courses": courses})
def section_page(request):
    return render(request, 'app1/section.html')

def gentimetable_page(request):
    return render(request, 'app1/gentimetable.html')
