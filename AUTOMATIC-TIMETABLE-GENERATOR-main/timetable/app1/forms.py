from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from .models import Course, Faculty



class CourseForm(forms.Form):
    course_id_validator = RegexValidator(
        regex=r'^\d{2}[A-Z]{2}\d{3}$',
        message="Invalid Format"
    )

    course_id = forms.CharField(
        validators=[
            MaxLengthValidator(limit_value=7, message="Course ID is not 7 characters"),
            course_id_validator,
        ]
    )
    course_name = forms.CharField(max_length=100)

    def clean_course_id(self):
        course_id = self.cleaned_data['course_id']
        existing_course = Course.objects.filter(cid=course_id).first()
        if existing_course:
            raise ValidationError(f"Course with ID '{course_id}' already exists with Name '{existing_course.cname}'.")
        return course_id

class FacultyForm(forms.Form):
    faculty_id_validator = RegexValidator(
        regex=r'^\d{5}$',
        message="Invalid Faculty ID Format"
    )

    faculty_id = forms.CharField(
        validators=[
            MinLengthValidator(limit_value=5, message="Faculty ID should be 5 digits"),
            MaxLengthValidator(limit_value=5, message="Faculty ID should be 5 digits"),
            faculty_id_validator,
        ]
    )
    faculty_name = forms.CharField(
        validators=[
            MinLengthValidator(limit_value=2, message="Faculty name is too short"),
            MaxLengthValidator(limit_value=25, message="Faculty name is too long"),
        ]
    )

    def clean_faculty_id(self):
        faculty_id = self.cleaned_data['faculty_id']
        existing_faculty = Faculty.objects.filter(fid=faculty_id).first()
        if existing_faculty:
            raise ValidationError(f"Faculty with ID '{faculty_id}' already exists with Name '{existing_faculty.fname}'.")
        return faculty_id

