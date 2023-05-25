from django.shortcuts import render,get_object_or_404
from articleapp.models import *
from django.contrib.auth.decorators import login_required

def home(request):
    data=Article.objects.all()
    return render(request,'articleapp/home.html',{'articles':data})


def view_art(request,art_id):
    data=get_object_or_404(Article,pk=art_id)
    return render(request,'articleapp/view_art.html',{'article':data})