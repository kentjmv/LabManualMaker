from tokenize import Name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User, Group
from ckeditor.fields import RichTextField

# Create your models here.
class user_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(null=True, blank=True, max_length=255)
    
    def __str__(self):
        return f"User {self.id} is {self.name}"

class Courses(models.Model):
    instructor = models.ForeignKey(user_info, on_delete=models.CASCADE, related_name="CourseInstructor")
    course_code = models.AutoField(primary_key=True)
    course_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    def __str__(self):
        return f"Instructor {self.instructor.user} is from {self.department} teaching {self.course_title}"

class Lab_Manual(models.Model):
    lab_name = models.CharField(max_length=255)
    instructor = models.ForeignKey(user_info, on_delete=models.CASCADE, related_name="LabInstructor")
    course_code = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="Courseinformation")
    activity_name = models.CharField(max_length=255)
    activity_no = models.FloatField()
    objectives = RichTextField(blank=True, null=True)
    ilo = RichTextField(blank=True, null=True)
    discussion = RichTextField(blank=True, null=True)
    resources = RichTextField(blank=True, null=True)
    procedure =RichTextField(blank=True, null=True)
    results = RichTextField(blank=True, null=True)
    supplementary = RichTextField(blank=True, null=True)
    observation = RichTextField(blank=True, null=True)
    conclusion = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"Activity {self.activity_no} entitled {self.activity_name}"

class Sharing(models.Model):
    LabManual = models.ForeignKey(Lab_Manual, on_delete=models.CASCADE, related_name="LabInformation")
    instructor = models.ForeignKey(user_info, on_delete=models.CASCADE, related_name="SharedTo")

    def __str__(self):
        return f"{self.LabManual.activity_name} is shared to {self.instructor.user}"