from django.shortcuts import render
import random
def home(request):
    l=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Big'):
        l+=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('Numbers'):
        l+=list('1234567890')
    if request.GET.get('Special'):
        l+=list('!@#$%^&*()_+|')
    lenght=int(request.GET.get('lenght',5))
    result=''
    for i in range(lenght):
        result+=random.choice(l)
    return render(request,'password/home.html',{'result':result})

def about(request):
    return render(request,'password/about.html')
# Create your views here.
