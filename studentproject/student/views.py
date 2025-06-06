from django.shortcuts import get_object_or_404, render
from student.models import Student
from django.http import*
from django.http import HttpResponse
 
# Create your views here.
def student_detail(request,pk):
    student=get_object_or_404(Student,pk=pk)
    context={
        'student':student
    }
    return render(request,'student_detail.html',context)
    #return HttpResponse(student)




