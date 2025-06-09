from django.http import HttpResponse

def home(request):
    return HttpResponse("<h4>This is my Home page</h4>")