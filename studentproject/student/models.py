from django.db import models

class Student(models.Model):
    Name=models.CharField(max_length=100)
    Course_Name=models.CharField(max_length=100)
    Student_Id=models.IntegerField()
    Email_address=models.EmailField(max_length=100,unique=True)
    Contact_No=models.CharField(max_length=100,blank=True)
    photo=models.ImageField(upload_to='images')
    Created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
           return self.Name


class course(models.Model):
    maths=models.CharField(max_length=100)
    Tamil=models.CharField(max_length=100)
    English=models.CharField(max_length=150)





