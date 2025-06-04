from django.http import HttpResponse
from django.shortcuts import render
from student.models import Student

def home(request):
    student=Student.objects.all()
    print(student)
    return render(request,'home.html')