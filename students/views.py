from django.shortcuts import render

# Create your views here.
def getstudenthome(request):
    return render(request, 'students_home.html')

def addstudents(request):
    return render(request, 'students_registration.html') 