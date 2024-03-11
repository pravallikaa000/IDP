from django.db import models

class Faculty(models.Model):
    fid = models.CharField(max_length=6 , primary_key=True)
    fname = models.CharField(max_length=25)
    
    def __str__(self):
        return f'{self.fid} {self.fname}'
    
    

class Course(models.Model):
    cid = models.CharField(max_length=7, primary_key=True)
    cname = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.cid} {self.cname}'
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cid', 'cname'], name='unique_course')
        ]
    
   
class Section(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name='sections')

    def __str__(self):
        return self.name

class TimetableEntry(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
   #  department = models.ForeignKey(Department, on_delete=models.CASCADE,default=1)
   #  time = models.ForeignKey(Time, on_delete=models.CASCADE)
   #  day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course} | {self.faculty} | {self.section}"
