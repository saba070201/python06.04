from django.shortcuts import render

def home(request):
    return render(request,'articleapp/home.html')
# Create your views here.
