from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(response):
    return HttpResponse("Hello, Django Beginner!")

def list_student(response):
    students=Student.objects.all()
    return HttpResponse(students)
