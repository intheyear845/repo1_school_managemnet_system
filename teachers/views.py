from django.shortcuts import render

# Create your views here.
def getteachershome(request):
    return render(request,'teachers_home.html')