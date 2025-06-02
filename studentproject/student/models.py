from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=150)


class Student(models.Model):
    name=models.CharField(max_length=150)
    age=models.IntegerField(null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)





